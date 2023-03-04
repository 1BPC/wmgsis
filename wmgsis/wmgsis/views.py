from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import calculate
from . models import Graduate
from . forms import GraduateForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request): 
    """ index function
    :param request: Http Request object
    :return: calls render function passing in a http request, the template and a payload 

    This function gets calls the calculate class and functions to get the data from the database
    Then passes the data into a context dictionary so can be accessed through the template """
    
    grad_data = calculate.Calculate_Grad()
    degree_class = grad_data.getDegreeClassData()
    salary_data = grad_data.getSalaryData()
    activity = grad_data.getGradActivity()
    
    context = {"grades":degree_class, "city":salary_data, "activity":activity}

    # render takes a request, a template and a payload to pass  
    return render(request, "index.html", context)

def delete_graduate(request, id):
    """ Delete Graduate Function
    :param request: Http Request object
    :param id: if of graduate to delete
    :return: returns HttpResponseRedirect and used reverse URL matching """
    
    graduate = Graduate.objects.get(id=id)
    graduate.delete()

    return HttpResponseRedirect(reverse('manage'))


def manage(request): 
    """ Manage Function
    :param request: Http Request object
    :return: calls render function passing in a http request, the template and a payload 

    This function creates a form instance from the POST data
    Then saves a new graduate object from the data
    Redirects to /manage if submitted is succesfull """
   
    # Grab all objects in the class and assign to variable 
    graduate_list = Graduate.objects.all()

    submitted = False

    if request.method == "POST":        
        form = GraduateForm(request.POST)
        print(request)
        
        if form.is_valid():
            form.save() 
            return HttpResponseRedirect('/manage?submitted=True')
        
    else: 
        form = GraduateForm
        if 'submmitted' in request.GET:
            submitted = True 
    
    context = { "form":form, 'submitted':submitted, "graduate_list": graduate_list}

    return render(request, "manage.html", context)


def health(request):
    return render(request, "health.html")


def demographic(request):
    return render(request, "demographic.html")


def success(request):
    return render(request, "success.html")


def satisfaction(request):
    return render(request, "satisfaction.html")
   

def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")



