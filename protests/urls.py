from django.urls import path
from .views import (
    protest_list,
    participant_list,
    protest_detail,
    create_protest,
    edit_protest,
)

urlpatterns = [
    path('', protest_list, name='protest_list'),
    path('participants/', participant_list, name='participant_list'),
    path('create/', create_protest, name='create_protest'),
    path('<int:protest_id>/', protest_detail, name='protest_detail'),
    path('<int:pk>/edit/', edit_protest, name='edit_protest'),
]
