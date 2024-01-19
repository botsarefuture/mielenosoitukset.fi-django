from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django import template

from organizations.forms import OrganizationForm
from organizations.models import Organization, Membership
from protests.models import Protest

register = template.Library()

def user_can_edit_organization(user, organization_id):
    if not user.is_authenticated:
        return False

    if user.is_superuser:
        return True

    user_instance = user
    organization_instance = get_object_or_404(Organization, id=organization_id)

    relationship_exists = Membership.objects.filter(user=user_instance, organization=organization_instance).exists()

    return relationship_exists

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations/organization_list.html', {'organizations': organizations})

@login_required
def register_organization(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            organization = form.save()
            Membership.objects.create(user=request.user, organization=organization, access_level='owner')
            return redirect('organization_list')
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
    fields = ['name', 'description', 'location', 'date_of_foundation', 'contact_email', 'website', 'activism_focus']
    success_url = reverse_lazy('organization_list')

    def test_func(self):
        organization_id = self.kwargs.get('pk')
        return user_can_edit_organization(self.request.user, organization_id)

    def form_valid(self, form):
        form.instance.modified_by = self.request.user
        return super().form_valid(form)
