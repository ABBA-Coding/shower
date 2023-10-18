from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    id = models.CharField("id", primary_key=True, max_length=25, db_index=True, unique=True)
    name = models.CharField("name", max_length=255)

    def __str__(self):
        return self.id


class Business(models.Model):
    class BusinessBudget(models.IntegerChoices):
        SMALL = 0, "Small"
        MEDIUM = 1, "Medium"
        LARGE = 2, "Large"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget = models.IntegerField(choices=BusinessBudget.choices, default=BusinessBudget.SMALL)
    website = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
