from django.contrib import admin
from django.urls import path, include
from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('todos.urls')),

    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]