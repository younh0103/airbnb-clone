# Generated by Django 5.0 on 2023-12-20 04:45

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_photo_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roomtype',
            options={'ordering': ['name'], 'verbose_name': 'Room Type'},
        ),
        migrations.AlterField(
            model_name='room',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
