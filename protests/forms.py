from django import forms
from .models import Protest

class ProtestForm(forms.ModelForm):
    class Meta:
        model = Protest
        fields = ['location', 'date', 'organization', 'topics', 'details']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
