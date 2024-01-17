# forms.py
from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name', 'description', 'location', 'date_of_foundation', 'contact_email', 'website', 'activism_focus', 'logo']
