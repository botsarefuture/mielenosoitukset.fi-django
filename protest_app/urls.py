from django.contrib import admin
from django.urls import path, include
from protests.views import front_page
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('protests/', include('protests.urls')),
    path('organizations/', include('organizations.urls')),
    path('topics/', include('topics.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This line is important for authentication URLs
    path('accounts/', include('users.urls')),  # You might have a separate app for user-related URLs
    path('', front_page, name='front_page'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
