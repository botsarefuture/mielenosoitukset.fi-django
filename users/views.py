# users/views.py
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.shortcuts import render, redirect

# users/views.py
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import the customized form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Use the customized form
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()  # Use the customized form

    return render(request, 'register.html', {'form': form})


# users/views.py
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful edit
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'profile_edit.html', {'form': form})

from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import ChangePasswordForm

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('password_change_done'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})

@login_required
def password_change_done(request):
    return render(request, 'password_change_done.html')