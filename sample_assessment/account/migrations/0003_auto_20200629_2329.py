# Generated by Django 3.0.7 on 2020-06-29 17:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
