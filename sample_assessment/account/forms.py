from django.forms import ModelForm
from .models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'phone_no', 'email', 'photo', 'account_type']
