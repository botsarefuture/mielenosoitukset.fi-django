# users/urls.py
from django.urls import path
from .views import register, profile, profile_edit
from .views import profile, change_password, password_change_done


from django.urls import path

   

urlpatterns = [
    path('register/', register, name='register'),
 path('profile/', profile, name='profile'),
    path('change-password/', change_password, name='change_password'),
    path('password-change-done/', password_change_done, name='password_change_done'),    path('profile/edit/', profile_edit, name='profile_edit'),



    # ... other URL patterns for your app
]
