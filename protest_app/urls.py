from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('protests/', include('protests.urls')),
    path('organizations/', include('organizations.urls')),
    path('topics/', include('topics.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This line is important for authentication URLs
    path('accounts/', include('users.urls')),  # You might have a separate app for user-related URLs
]
