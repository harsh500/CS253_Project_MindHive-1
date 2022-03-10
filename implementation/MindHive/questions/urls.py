from django.urls import path

from . import views

urlpatterns = [
    # eg: /questions/1/
    path('<int:question_id>', views.view, name='view_question'),
    # eg: /questions/edit/1/
    path('<int:question_id>/edit/', views.edit, name='edit_question'),
    # eg: /questions/ask/
    path('<int:user_id>/ask/', views.ask, name='ask'),
    path('<int:user_id>/ask/submit', views.submit, name='submit')
]