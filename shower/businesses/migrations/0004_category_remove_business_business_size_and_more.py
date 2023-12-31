# Generated by Django 4.2.6 on 2023-10-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("businesses", "0003_alter_sites_business"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.CharField(
                        db_index=True, max_length=25, primary_key=True, serialize=False, unique=True, verbose_name="id"
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
            ],
        ),
        migrations.RemoveField(
            model_name="business",
            name="business_size",
        ),
        migrations.RemoveField(
            model_name="business",
            name="industry",
        ),
        migrations.AddField(
            model_name="business",
            name="budget",
            field=models.IntegerField(choices=[(0, "Small"), (1, "Medium"), (2, "Large")], default=0),
        ),
        migrations.AddField(
            model_name="business",
            name="category",
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to="businesses.category"),
            preserve_default=False,
        ),
    ]
