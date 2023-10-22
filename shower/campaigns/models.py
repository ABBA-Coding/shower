from django.db import models


class Campaign(models.Model):
    class CampaignStatusChoices(models.IntegerChoices):
        DRAFT = 0, "DRAFT"
        ACTIVE = 1, "ACTIVE"
        DISABLED = 2, "DISABLED"

    class CampaignPlatformChoice(models.TextChoices):
        GOOGLE = "google", "google"
        MICROSOFT = "microsoft", "microsoft"
        FACEBOOK = "facebook", "facebook"
        INSTAGRAM = "instagram", "instagram"
        TWITTER = "twitter", "twitter"
        BANNER = "banner", "banner"

    class CampaignLanguageChoices(models.TextChoices):
        ENGLISH = "english", "english"
        RUSSIAN = "russian", "russian"
        OTHER = "other", "other"

    name = models.CharField(max_length=90)
    business = models.ForeignKey("businesses.Business", on_delete=models.CASCADE, related_name="campaigns")
    website = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    language = models.CharField(max_length=10, choices=CampaignLanguageChoices.choices)
    status = models.IntegerField(
        choices=CampaignStatusChoices.choices,
        default=CampaignStatusChoices.DRAFT,
        editable=False)
    platform = models.CharField(max_length=10, choices=CampaignPlatformChoice.choices)

    purpose = models.CharField(max_length=255, null=True, blank=True)
    cell_phone = models.CharField(max_length=20, null=True, blank=True)
    website_page_url = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    def __str__(self):
        return self.website


class CampaignDescriptions(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="descriptions")
    text = models.CharField(max_length=90)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Campaign Description"
        verbose_name_plural = "Campaigns Descriptions"


class CampaignHeadlines(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="headlines")
    text = models.CharField(max_length=90)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Campaign Headline"
        verbose_name_plural = "Campaign Headlines"
