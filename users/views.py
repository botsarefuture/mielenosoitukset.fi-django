# users/views.py
from typing import Dict

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse

from organizations.models import Membership
from .forms import CustomUserCreationForm, CustomUserChangeForm, ChangePasswordForm
from users.models import CustomUser  # Replace with the actual import path for your CustomUser model


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})



def get_user_organizations_access(user_id: int) -> Dict[str, str]:
    try:
        # Retrieve the user object
        user = CustomUser.objects.get(id=user_id)

        # Retrieve the user's memberships and related organizations with access levels
        user_memberships = Membership.objects.filter(user=user)
        
        return user_memberships

    except CustomUser.DoesNotExist:
        # Handle the case where the user does not exist
        return {}




@login_required
def profile(request):
    return render(request, 'users/profile.html', context={"info": get_user_organizations_access(request.user.id)})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'users/profile_edit.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('password_change_done'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)

    return render(request, 'users/change_password.html', {'form': form})

@login_required
def password_change_done(request):
    return render(request, 'users/password_change_done.html')

def custom_logout(request):
    # Store the current URL in the session
    request.session['pre_logout_url'] = request.META.get('HTTP_REFERER', '/')
    
    # Logout the user
    logout(request)
    
    # Redirect to the stored URL or a default URL if not available
    return redirect(request.session.get('pre_logout_url', '/'))