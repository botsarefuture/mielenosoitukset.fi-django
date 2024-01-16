from django.urls import path
from .views import topic_list, topic_detail

urlpatterns = [
    path('topics/', topic_list, name='topic_list'),
    path('<int:topic_id>/', topic_detail, name='topic_detail'),

]
