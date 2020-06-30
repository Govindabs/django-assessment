from django.contrib import admin
from .models import *


class AccountAdmin(admin.ModelAdmin):
    list_display = ['account_id', 'account_type']


class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'name', 'phone_no', 'email', 'account_type']


# Register your models here.
admin.site.register(Account, AccountAdmin)
admin.site.register(User, UserAdmin)
