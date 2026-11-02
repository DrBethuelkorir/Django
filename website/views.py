from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def login_user(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print("LOGIN ATTEMPT:", username, user)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in.")
            return redirect('home')

        messages.error(request, "Invalid credentials")

    return render(request, 'home.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')