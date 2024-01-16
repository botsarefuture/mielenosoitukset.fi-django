from django.urls import path
from .views import organization_list, register_organization, organization_detail, CustomLoginView, OrganizationUpdateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', organization_list, name='organization_list'),
    path('register/', register_organization, name='register_organization'),
    path('<int:organization_id>/', organization_detail, name='organization_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('<int:pk>/update/', OrganizationUpdateView.as_view(), name='organization_update'),




]