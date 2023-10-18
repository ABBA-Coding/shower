from django.db import models


class Campaign(models.Model):
    business = models.OneToOneField("businesses.Business", on_delete=models.CASCADE, related_name="campaign")
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.website

    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"


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
