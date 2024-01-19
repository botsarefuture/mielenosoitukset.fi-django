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
        model = CustomUser
        fields = ["email", "username"]  # Specify the fields you want for user creation
        # You can add more fields as needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'