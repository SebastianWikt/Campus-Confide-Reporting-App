from django.contrib import admin
from django.urls import path, include
from hooknowsapp import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.homepage, name='home'),
]