from django.contrib import admin
from django.urls import path, include
from hooknowsapp import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('create_report/', views.create_report, name='create_report'),
    path('view_reports/', views.view_reports, name='view_reports'),
    path('report_submited/', views.report_submitted, name = 'report_submitted')
]