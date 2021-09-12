from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('givekudo/', views.givekudo, name='givekudo'),
    path('dashboard/', views.dashboard, name='dashboard')

]