# users/forms.py
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']  # Add or remove fields based on your requirements

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)  # Exclude the 'password' field

class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["email"]
        model = CustomUser
