from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from .forms import (
    RegisterForm,
    LoginForm,
    ResetPasswordForm,
    ResetPasswordNewPassword,)
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from sessions_order.cart import Cart
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView)
from django.contrib.messages.views import SuccessMessageMixin

User = get_user_model()


class ShopResetPasswordView(SuccessMessageMixin, PasswordResetView):
    """ enter email to check email"""

    template_name = 'account/reset_password.html'
    email_template_name = 'account/reset_password_email.html'
    subject_template_name = 'account/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password_reset_done')


class ShopPasswordResetDoneView(PasswordResetDoneView):
    """ this is where say email sent to your email """

    template_name = 'account/password_reset_done.html'


class ShopPasswordResetConfirmView(PasswordResetConfirmView):
    """ this is where you change your old password to new one """

    template_name = 'account/password_reset_page.html'


class ShopPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


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
                cart = Cart(request)
                cart.user_login()
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
            User.objects.create_user(
                username=username, password=password, email=email)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
