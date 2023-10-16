# serializers.py
from rest_framework import serializers
from .models import Business, Sites


class BusinessCreateSerializer(serializers.ModelSerializer):
    website = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = Business
        exclude = ("user",)

    def create(self, validated_data):
        website_data = validated_data.pop('website')
        request = self.context.get('request')
        user = request.user
        business = Business.objects.create(user=user, **validated_data)
        Sites.objects.create(business=business, url=website_data)
        return business


class SitesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Sites


class BusinessListSerializer(serializers.ModelSerializer):
    websites = SitesSerializer(many=True)

    class Meta:
        model = Business
        fields = "__all__"

