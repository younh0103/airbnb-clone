# Generated by Django 5.0 on 2023-12-12 07:01

import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomType",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="room",
            name="country",
            field=django_countries.fields.CountryField(default="", max_length=2),
        ),
        migrations.AddField(
            model_name="room",
            name="room_type",
            field=models.ManyToManyField(blank=True, to="rooms.roomtype"),
        ),
    ]
