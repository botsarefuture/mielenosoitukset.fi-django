# users/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CustomUserCreationForm, CustomUserChangeForm, ChangePasswordForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'profile_edit.html', {'form': form})

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

    return render(request, 'change_password.html', {'form': form})

@login_required
def password_change_done(request):
    return render(request, 'password_change_done.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    # Store the current URL in the session
    request.session['pre_logout_url'] = request.META.get('HTTP_REFERER', '/')
    
    # Logout the user
    logout(request)
    
    # Redirect to the stored URL or a default URL if not available
    return redirect(request.session.get('pre_logout_url', '/'))