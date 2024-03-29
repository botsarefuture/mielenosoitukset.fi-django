from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .views import (
    protest_list, participant_list, protest_detail,
    create_protest, edit_protest, front_page, delete_protest
)
from .sitemaps import ProtestSitemap

urlpatterns = [
    path('', protest_list, name='protest_list'),
    path('participants/', participant_list, name='participant_list'),
    path('<int:protest_id>/', protest_detail, name='protest_detail'),
    path('create_protest/', create_protest, name='create_protest'),
    path('edit_protest/<int:pk>/', edit_protest, name='edit_protest'),
    path('front_page/', front_page, name='front_page'),
    path('delete_protest/<int:pk>/', delete_protest, name='delete_protest'),
    path("sitemap.xml", sitemap, {"sitemaps": {'protests': ProtestSitemap}}, name="django.contrib.sitemaps.views.sitemap"),
]
