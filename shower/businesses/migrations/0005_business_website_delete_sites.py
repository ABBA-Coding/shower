# Generated by Django 4.2.6 on 2023-10-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0004_category_remove_business_business_size_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="business",
            name="website",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Sites",
        ),
    ]
