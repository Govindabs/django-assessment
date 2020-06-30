# Generated by Django 3.0.7 on 2020-06-29 17:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('phone_no', models.PositiveIntegerField(validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxValueValidator(9999999999)])),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('account_type', models.ForeignKey(db_column='account', on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
        ),
    ]