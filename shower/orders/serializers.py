from rest_framework import serializers
from .models import Order, PriceList
from ..utils.payment import create_invoice


class OrderListSerializer(serializers.ModelSerializer):
    campaign_name = serializers.StringRelatedField(source="campaign.name")
    class Meta:
        model = Order
        fields = "__all__"


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = "__all__"


class OrderCreateSerializer(serializers.ModelSerializer):
    invoice_id = serializers.CharField(read_only=True)

    class Meta:
        model = Order
        exclude = "status", "created_at"

    def create(self, validated_data):
        amount = validated_data.get('amount')
        currency = validated_data.get('currency')
        campaign_id = validated_data.get('campaign')
        is_success, invoice_response = create_invoice(amount, currency, campaign_id)
        if is_success:
            validated_data['invoice_id'] = invoice_response.get('invoice')
            order = Order.objects.create(**validated_data)
            return order
        else:
            raise serializers.ValidationError("Failed to create the invoice. Please try again later.")
