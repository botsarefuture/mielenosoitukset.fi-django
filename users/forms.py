from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser  # Adjust the import based on your actual UserProfile model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']  # Add or remove fields based on your requirements

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)  # Exclude the 'password' field

from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser  # Adjust the import based on your actual UserProfile model

# users/forms.py
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ["email"]

        model = CustomUser
