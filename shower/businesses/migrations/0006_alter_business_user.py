# Generated by Django 4.2.6 on 2023-10-18 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("businesses", "0005_business_website_delete_sites"),
    ]

    operations = [
        migrations.AlterField(
            model_name="business",
            name="user",
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]