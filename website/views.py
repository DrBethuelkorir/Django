from urllib import request

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


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

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            #authenticate and log in the user after registration

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username=username, password=password)
            login(request, user)
            messages.success(request, "You have been registered and logged in.")
            return redirect('home')

    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})