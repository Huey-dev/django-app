from django.urls import path
from . import views

app_name = 'taskapp'
urlpatterns = [
    path("", views.index, name='index'),
    path("add_task_form/", views.add_task_form, name="add_task_form")
]