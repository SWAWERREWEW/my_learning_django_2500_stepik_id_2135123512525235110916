# sitewomen\users\urls.py
from django.urls import path
from . import views

app_name = "users"

"""Не забывать в конце пути ставить слеш /"""
urlpatterns = [
    # users:
    # users:login
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
