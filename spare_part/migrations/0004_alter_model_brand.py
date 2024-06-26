# Generated by Django 5.0.6 on 2024-06-06 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spare_part", "0003_brand_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="model",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="models",
                to="spare_part.brand",
            ),
        ),
    ]
