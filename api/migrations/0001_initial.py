# Generated by Django 5.0.6 on 2024-07-11 14:16

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
                        default=uuid.UUID("61080053-13e3-4ca8-a00a-7d61ba92262d"),
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
