from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_type = models.CharField(unique=True, max_length=25)

    def __str__(self):
        return self.account_type


class User(models.Model):
    REQUEST_STATUS = (
        ('pending', 'PENDING'),
        ('confirmed', 'CONFIRMED'),
        ('rejected', 'REJECTED')
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    phone_no = PhoneNumberField()
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to='profile_pics')
    account_type = models.ForeignKey('Account', db_column='account', on_delete=models.CASCADE)
    req_status = models.CharField(max_length=9, choices=REQUEST_STATUS, default='pending')

    def __str__(self):
        return self.name
