# Generated by Django 2.0 on 2018-09-22 05:16

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Tip",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("text", models.TextField()),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[
                            (10, "debug"),
                            (20, "info"),
                            (25, "success"),
                            (30, "warning"),
                            (40, "error"),
                        ],
                        default=20,
                    ),
                ),
                ("run_start", models.DateTimeField(default=django.utils.timezone.now)),
                ("run_end", models.DateTimeField(blank=True, null=True)),
                ("view", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "seen_by",
                    models.ManyToManyField(
                        blank=True,
                        related_name="seen_tips",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("sites", models.ManyToManyField(to="sites.Site")),
            ],
        )
    ]
