from django.contrib import admin
from django.urls import path, include
from protests.views import front_page
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from organizations.sitemap import OrganizationSitemap
from protests.sitemaps import ProtestSitemap  # Import the ProtestSitemap

sitemaps = {
    'organizations': OrganizationSitemap,
    'protests': ProtestSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('protests/', include('protests.urls')),
    path('organizations/', include('organizations.urls')),
    path('topics/', include('topics.urls')),
    
    # User-related URLs
    path('accounts/', include('users.urls')), 
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    
    path('', front_page, name='front_page'),

    # Sitemap
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
