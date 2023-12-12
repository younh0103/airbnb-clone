# Generated by Django 5.0 on 2023-12-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_avatar_user_gender"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birthdate",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="currency",
            field=models.CharField(
                blank=True,
                choices=[("usd", "USD"), ("krw", "KRW")],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="language",
            field=models.CharField(
                blank=True, choices=[("en", "english"), ("kr", "korean")], max_length=2
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="superhost",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("male", "male"), ("female", "female"), ("other", "other")],
                max_length=10,
                null=True,
            ),
        ),
    ]
