from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.todo_list, name="list"),
    path("create/", views.todo_create, name="create"),
    path("delete/<int:id>/", views.todo_delete, name="delete"),
    path("edit/<int:id>/", views.todo_edit, name="edit"),
    path("complete/<int:id>/", views.todo_complete, name="complete"),
]

