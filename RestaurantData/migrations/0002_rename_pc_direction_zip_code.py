# Generated by Django 3.2.9 on 2021-11-24 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantData', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direction',
            old_name='pc',
            new_name='zip_code',
        ),
    ]
