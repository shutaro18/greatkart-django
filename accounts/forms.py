from django import forms
from django.contrib.auth import models
from .models import Account


class RegistraionForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']