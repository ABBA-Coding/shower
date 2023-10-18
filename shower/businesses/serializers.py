from rest_framework import serializers
from .models import Business, Category
from ..campaigns.serializers import CampaignListSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BusinessCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        exclude = ("user",)


class BusinessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = "__all__"


class BusinessDetailSerializer(serializers.ModelSerializer):
    campaigns = CampaignListSerializer(many=True)

    class Meta:
        model = Business
        fields = "__all__"
