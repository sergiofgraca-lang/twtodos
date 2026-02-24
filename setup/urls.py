from django.contrib import admin
from django.urls import path
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.todo_list, name='todos:list'),
    path('create/', views.todo_create, name='create'),
    path('delete/<int:id>/', views.todo_delete, name='delete'),
    path('edit/<int:id>/', views.todo_edit, name='edit'),
    path('complete/<int:id>/', views.todo_complete, name='complete'),

    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]