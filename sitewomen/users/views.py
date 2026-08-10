# sitewomen/users/views.py
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_user(request):
    return HttpResponse("login🛠📥🌎")


def logout_user(request):
    return HttpResponse("logout🛠📤🗝")
