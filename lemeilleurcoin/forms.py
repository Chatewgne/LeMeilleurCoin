# accounts/forms.py
from django import forms
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

# Extend user creation form with phone number
class CustomUserCreationForm(UserCreationForm):
    """
    Extend user creation form with phone number
    """

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number")


# Extend user change form with phone number
class CustomUserChangeForm(UserChangeForm):
    """
    Extend user change form with phone number
    """

    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone_number")
