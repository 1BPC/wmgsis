from django.shortcuts import render
from django.http import HttpResponse
from . import calculate



def index(request): 
    grad_data = calculate.Calculate_Grad()

    degree_class = grad_data.getDegreeClassData()
    salary_data = grad_data.getSalaryData()
    activity = grad_data.getGradActivity()

    context = {"grades":degree_class, "city":salary_data, "activity":activity}

    return render(request, "index.html", context)


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

