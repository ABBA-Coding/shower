# Generated by Django 4.2.6 on 2023-10-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="business",
            name="url",
        ),
        migrations.AlterField(
            model_name="business",
            name="business_size",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="business",
            name="industry",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
