# Generated by Django 4.2.6 on 2023-10-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0005_remove_pricelist_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="amount",
            field=models.BigIntegerField(),
        ),
    ]