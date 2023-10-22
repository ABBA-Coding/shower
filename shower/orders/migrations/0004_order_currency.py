# Generated by Django 4.2.6 on 2023-10-22 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_alter_order_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="currency",
            field=models.CharField(
                choices=[("btc", "btc"), ("ltc", "ltc"), ("bch", "bch"), ("doge", "doge")], default="btc", max_length=5
            ),
            preserve_default=False,
        ),
    ]
