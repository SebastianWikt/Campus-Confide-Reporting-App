import users
from django.contrib import admin
from django.urls import path, include
from hooknowsapp import views

urlpatterns = [
    path('', views.login_view, name='login'),  # Updated to 'login_view'
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),  # Ensure this points to the 'home' view
]