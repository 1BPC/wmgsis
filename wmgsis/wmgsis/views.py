from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    #print(request.user)  # .user is user object of the current session
    return render(request, "index.html")


def graduate(request):
    return render(request, "graduate.html")


def health(request):
    return render(request, "health.html")


def demographic(request):
    return render(request, "demographic.html")


def success(request):
    return render(request, "success.html")


def satisfaction(request):
    return render(request, "satisfaction.html")
   
   
def profile(request):
    return render(request, "profile.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def settings(request):
    return render(request, "settings.html")

    jlhj