from rest_framework import serializers, status
from .models import Business, Category
from rest_framework.response import Response
from ..campaigns.serializers import CampaignListSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = ("user",)

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        business = Business.objects.create(user=user, **validated_data)
        return business

class BusinessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"


class BusinessDetailSerializer(serializers.ModelSerializer):
    campaigns = CampaignListSerializer(many=True)

    class Meta:
        model = Business
        fields = "__all__"
