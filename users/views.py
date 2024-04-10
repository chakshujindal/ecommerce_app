from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.urls import reverse_lazy

# Create your views here.

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Implement other views for login, logout, password reset, etc.

class Login(LoginView):
    template_name = 'login.html'  # Path to your login template
    success_url = reverse_lazy('home')  # Redirect to home page after login

class Logout(LogoutView):
    next_page = reverse_lazy('home')  # Redirect to home page after logout

class PasswordReset(PasswordResetView):
    template_name = 'password_reset.html'  # Path to your password reset template
    email_template_name = 'password_reset_email.html'  # Path to your password reset email template
    success_url = reverse_lazy('password_reset_done')  # Redirect to password reset done page

class PasswordResetDone(PasswordResetDoneView):
    template_name = 'password_reset_done.html'  # Path to your password reset done template
