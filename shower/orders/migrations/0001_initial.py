# Generated by Django 4.2.6 on 2023-10-20 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("campaigns", "0003_campaign_cell_phone_campaign_country_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PriceList",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.IntegerField()),
                (
                    "currency",
                    models.CharField(
                        choices=[("btc", "btc"), ("ltc", "ltc"), ("bch", "bch"), ("doge", "doge")], max_length=5
                    ),
                ),
                ("days", models.IntegerField()),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
            ],
            options={
                "verbose_name": "Price list",
                "verbose_name_plural": "Price list",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.IntegerField()),
                ("days", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "CREATED"), (1, "PAID"), (2, "EXPIRED")], default=0, editable=False
                    ),
                ),
                ("invoice_id", models.CharField(db_index=True, max_length=50)),
                (
                    "campaign",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="orders", to="campaigns.campaign"
                    ),
                ),
            ],
            options={
                "verbose_name": "Order",
                "verbose_name_plural": "Orders",
            },
        ),
    ]