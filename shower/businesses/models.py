from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True, null=True)
    business_size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


class Sites(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name="websites")
    url = models.CharField("URL", max_length=255)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"
