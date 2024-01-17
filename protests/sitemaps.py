from django.contrib.sitemaps import Sitemap
from .models import Protest

class ProtestSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.6

    def items(self):
        return Protest.objects.all()

    def lastmod(self, obj):
        return obj.date

