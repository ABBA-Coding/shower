from django.db import models

from shower.campaigns.models import Campaign


class OrderCurrencyChoice(models.TextChoices):
    BTC = "btc", "btc"
    LTC = "ltc", "ltc"
    BCH = "bch", "bch"
    DOGE = "doge", "doge"


class PriceList(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=5, choices=OrderCurrencyChoice.choices)
    days = models.IntegerField()
    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        verbose_name = "Price list"
        verbose_name_plural = "Price list"

    def __str__(self):
        return "{} | {}".format(self.amount, self.currency)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()


class Order(models.Model):
    class OrderStatusChoices(models.IntegerChoices):
        CREATED = 0, "CREATED"
        PAID = 1, "PAID"
        EXPIRED = 2, "EXPIRED"
        PARTPAID = 3, "PARTPAID"

    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE, related_name="orders")
    amount = models.IntegerField()
    days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=OrderStatusChoices.choices, default=OrderStatusChoices.CREATED, editable=False)
    invoice_id = models.CharField(max_length=50, db_index=True, editable=False)


    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def save(self, *args, **kwargs):
        if self.status == self.OrderStatusChoices.PAID:
            self.campaign.status = Campaign.CampaignStatusChoices.ACTIVE
            self.campaign.save()
        super().save(*args, **kwargs)
