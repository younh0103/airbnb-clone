# Generated by Django 5.0 on 2023-12-13 01:55

import django.db.models.deletion
import django_countries.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Amenity",
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
                "verbose_name_plural": "Amenities",
            },
        ),
        migrations.CreateModel(
            name="Facility",
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
                "verbose_name_plural": "Facilities",
            },
        ),
        migrations.CreateModel(
            name="HouseRule",
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
                "verbose_name": "House Rule",
            },
        ),
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
                "verbose_name": "Room Type",
            },
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=140)),
                ("description", models.TextField()),
                (
                    "country",
                    django_countries.fields.CountryField(default="", max_length=2),
                ),
                ("city", models.CharField(max_length=80)),
                ("price", models.IntegerField()),
                ("address", models.CharField(max_length=140)),
                ("guests", models.IntegerField()),
                ("beds", models.IntegerField()),
                ("bedrooms", models.IntegerField()),
                ("baths", models.IntegerField()),
                ("check_in", models.TimeField()),
                ("check_out", models.TimeField()),
                ("instant_book", models.BooleanField(default=False)),
                ("amenities", models.ManyToManyField(blank=True, to="rooms.amenity")),
                ("facility", models.ManyToManyField(blank=True, to="rooms.facility")),
                (
                    "host",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "house_rule",
                    models.ManyToManyField(blank=True, to="rooms.houserule"),
                ),
                (
                    "room_type",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="rooms.roomtype",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Photo",
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
                ("caption", models.CharField(max_length=80)),
                ("file", models.ImageField(upload_to="")),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rooms.room"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]