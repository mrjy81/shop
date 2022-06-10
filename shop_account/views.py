from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('username', 'کاربر یافت نشد')
    context = {
        'form': form,
    }
    return render(request, 'account/login.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password=password, email=email)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
