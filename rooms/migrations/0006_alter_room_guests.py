# Generated by Django 5.0 on 2024-01-04 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_roomtype_options_alter_room_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying ?'),
        ),
    ]