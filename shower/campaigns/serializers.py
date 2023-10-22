from rest_framework import serializers
from .models import Campaign, CampaignDescriptions, CampaignHeadlines


class CampaignUpdateSerializer(serializers.ModelSerializer):
    descriptions = serializers.ListField(write_only=True, required=False)
    headlines = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Campaign
        exclude = ("business",)

    def update(self, instance, validated_data):
        descriptions_data = validated_data.pop("descriptions", None)
        headlines_data = validated_data.pop('headlines', None)
        instance = super().update(instance, validated_data)
        if descriptions_data:
            CampaignDescriptions.objects.filter(campaign=instance).delete()
            CampaignDescriptions.objects.bulk_create(
                [
                    CampaignDescriptions(campaign=instance, text=description)
                    for description in descriptions_data
                ]
            )

        if headlines_data:
            CampaignHeadlines.objects.filter(campaign=instance).delete()
            CampaignHeadlines.objects.bulk_create(
                [
                    CampaignHeadlines(campaign=instance, text=headline)
                    for headline in headlines_data
                ]
            )
        return instance


class CampaignCreateSerializer(serializers.ModelSerializer):
    descriptions = serializers.ListField(write_only=True, required=False)
    headlines = serializers.ListField(write_only=True, required=False)

    class Meta:
        model = Campaign
        fields = "__all__"

    def create(self, validated_data):
        descriptions_data = validated_data.pop('descriptions', None)
        headlines_data = validated_data.pop('headlines', None)
        instance = super().create(validated_data)
        if descriptions_data:
            CampaignDescriptions.objects.bulk_create(
                [
                    CampaignDescriptions(campaign=instance, text=description)
                    for description in headlines_data
                ]
            )

        if headlines_data:
            CampaignHeadlines.objects.bulk_create(
                [
                    CampaignHeadlines(campaign=instance, text=headline)
                    for headline in headlines_data
                ]
            )

        return instance


class CampaignListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'website', "status", "platform")
