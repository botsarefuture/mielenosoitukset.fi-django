# organizations/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Organization
from protests.models import Protest  # Import the Protest model
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from users.models import CustomUser
from .forms import OrganizationForm
from .models import Membership
from django import template
from django.contrib.auth.decorators import login_required  # Add this import


register = template.Library()

from django.contrib.auth import get_user_model
from organizations.models import Organization, Membership

def user_can_edit_organization(user, organization_id):
    # Check if the user is authenticated
    if not user.is_authenticated:
        return False

    # Check if the user is a superuser
    if user.is_superuser:
        return True

    # Get instances of user and organization
    user_instance = get_user_model().objects.get(id=user.id)
    organization_instance = Organization.objects.get(id=organization_id)

    # Check if the user has a membership relationship with the organization
    relationship_exists = Membership.objects.filter(user=user_instance, organization=organization_instance).exists()

    return relationship_exists

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations/organization_list.html', {'organizations': organizations})

@login_required  # Add this decorator
def register_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')  # Redirect to the organization list page
    else:
        form = OrganizationForm()

    return render(request, 'organizations/register_organization.html', {'form': form})

def organization_detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    demonstrations = Protest.objects.filter(organization=organization)
    return render(request, 'organizations/organization_detail.html', {'organization': organization, 'demonstrations': demonstrations, 'user_can_edit_organization': user_can_edit_organization(request.user, organization_id)})

class CustomLoginView(LoginView):
    template_name = 'your_login_template.html'

class OrganizationUpdateView(UserPassesTestMixin, UpdateView):
    model = Organization
    template_name = 'organizations/organization_update.html'
    fields = ['name', 'description', 'location', 'date_of_foundation', 'contact_email', 'website', 'activism_focus']  # Add other fields as needed
    success_url = reverse_lazy('organization_list')  # Change to your desired success URL

    def test_func(self):
        # Check if the user is authenticated and has the necessary permissions
        organization_id = self.kwargs.get('pk')
        return user_can_edit_organization(self.request.user, organization_id)

    def form_valid(self, form):
        # Save the user making the change to the organization
        form.instance.modified_by = self.request.user
        return super().form_valid(form)