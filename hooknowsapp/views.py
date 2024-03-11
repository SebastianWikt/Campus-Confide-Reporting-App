from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        return render(request, 'hooknowsapp/login.html')

@login_required
def home(request):
    return render(request, 'hooknowsapp/homepage.html')


def logout_view(request):
    logout(request)
    return redirect("/")

def create_report(request):
    return render(request, 'hooknowsapp/create_report.html')
