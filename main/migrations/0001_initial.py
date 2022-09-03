# Generated by Django 4.1 on 2022-09-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("original_url", models.URLField(max_length=256)),
                ("hash", models.CharField(max_length=10)),
                ("created_at", models.DateTimeField(verbose_name="created at")),
            ],
        ),
    ]
