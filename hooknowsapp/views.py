from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'hooknowsapp/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'hooknowsapp/login.html')


def homepage(request):
    return render(request, 'hooknowsapp/homepage.html', {'username': request.user.username})
