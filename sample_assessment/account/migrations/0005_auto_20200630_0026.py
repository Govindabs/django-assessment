# Generated by Django 3.0.7 on 2020-06-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200629_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
