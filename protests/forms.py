from django import forms
from .models import Protest
from organizations.models import Organization, Membership
from django.contrib.auth import get_user_model

class ProtestForm(forms.ModelForm):
    date = forms.DateTimeField(
        label='Date and Time:',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Adjust the format as needed
        help_text='Format: YYYY-MM-DDTHH:MM'
    )

    class Meta:
        model = Protest
        fields = ['title', 'location', 'date', 'organization', 'topics', 'details', 'image']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Filter organizations based on whether the user can edit them
        self.fields['organization'].queryset = self.get_editable_organizations(user)

    def get_editable_organizations(self, user):
        # Check if the user is authenticated
        if not user.is_authenticated:
            return Organization.objects.none()

        # Check if the user is a superuser
        if user.is_superuser:
            return Organization.objects.all()

        # Get organizations where the user has a membership relationship
        user_instance = get_user_model().objects.get(id=user.id)
        editable_organizations = Membership.objects.filter(user=user_instance).values_list('organization', flat=True)

        return Organization.objects.filter(id__in=editable_organizations)
