from .models import Organization
from django.shortcuts import render, redirect
from .forms import OrganizationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import Organization
from .forms import OrganizationForm

def user_can_edit_organization(user, organization_id):
    # Implement your logic to check if the user has permission to edit the organization
    # For example, you might check if the user is a member or has a specific role in the organization
    # Replace this with your actual logic
    return user.is_authenticated and user.profile.organization.id == organization_id


def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

def register_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')  # Redirect to the organization list page
    else:
        form = OrganizationForm()

    return render(request, 'register_organization.html', {'form': form})

# organizations/views.py
from django.shortcuts import render, get_object_or_404
# organizations/views.py
from django.shortcuts import render, get_object_or_404
from .models import Organization
from protests.models import Protest  # Import the Protest model

def organization_detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    demonstrations = Protest.objects.filter(organization=organization)
    return render(request, 'organization_detail.html', {'organization': organization, 'demonstrations': demonstrations})

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'your_login_template.html'
    
from django.views.generic.edit import UpdateView
from .models import Organization
from users.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

class OrganizationUpdateView(UserPassesTestMixin, UpdateView):
    model = Organization
    template_name = 'organization_update.html'
    fields = ['name', 'founding_date', 'description']  # Add other fields as needed
    success_url = reverse_lazy('organization_list')  # Change to your desired success URL

    def test_func(self):
        organization_id = self.kwargs['pk']
        user = self.request.user

        # Check if the user is authenticated and has the necessary permissions
        return user.is_authenticated and user.organization.id == organization_id

    def form_valid(self, form):
        # Save the user making the change to the organization
        form.instance.modified_by = self.request.user
        return super().form_valid(form)