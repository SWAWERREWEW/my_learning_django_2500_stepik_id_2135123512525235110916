# sitewomen\users\urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "users"

"""Не забывать в конце пути ставить слеш /"""
urlpatterns = [
    # users:
    # users:login
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]
