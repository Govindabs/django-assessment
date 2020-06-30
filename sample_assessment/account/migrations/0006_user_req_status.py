# Generated by Django 3.0.7 on 2020-06-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200630_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='req_status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('confirmed', 'CONFIRMED'), ('rejected', 'REJECTED')], default='pending', max_length=9),
        ),
    ]