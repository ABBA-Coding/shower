from django.contrib import admin

from shower.campaigns.models import Campaign, CampaignDescriptions, CampaignHeadlines


class CampaignDescriptionInline(admin.TabularInline):
    model = CampaignDescriptions
    extra = 0


class CampaignHeadlineInline(admin.TabularInline):
    model = CampaignHeadlines
    extra = 0


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    inlines = [CampaignHeadlineInline, CampaignDescriptionInline]
