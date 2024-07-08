# Generated by Django 5.0.6 on 2024-07-08 13:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Books",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.UUID("ba1efa74-e417-4c7a-aeea-7388bc3fdbcf"),
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=400)),
            ],
        ),
    ]
