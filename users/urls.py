# users/urls.py
from django.urls import path
from .views import register, profile, profile_edit, change_password, password_change_done, custom_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('change-password/', change_password, name='change_password'),
    path('password-change-done/', password_change_done, name='password_change_done'),
    path('logout/', custom_logout, name='custom_logout'),

    # ... other URL patterns for your app
]
