
from django.urls import path
from . import views

urlpatterns = [
    # eg: /users/1/
    path('<int:user_id>', views.view, name='view_user'),
     # eg: /users/1/edit/
    path('<int:user_id>/edit', views.ask, name='edit_users'),
]