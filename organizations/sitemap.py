from django.contrib.sitemaps import Sitemap
from .models import Organization

class OrganizationSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.8

    def items(self):
        return Organization.objects.all()

    def lastmod(self, obj):
        return obj.date_of_foundation  # You can replace this with any relevant date field

