from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import calculate
from . models import Graduate
from . forms import GraduateForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request): 
    grad_data = calculate.Calculate_Grad()
    degree_class = grad_data.getDegreeClassData()
    salary_data = grad_data.getSalaryData()
    activity = grad_data.getGradActivity()
    
    context = {"grades":degree_class, "city":salary_data, "activity":activity}

    # render takes a request, a template and a payload to pass  
    return render(request, "index.html", context)

# remove
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
   

def delete_graduate(request, id):
    graduate = Graduate.objects.get(id=id)
    graduate.delete()

    return HttpResponseRedirect(reverse('manage'))


def manage(request): 
    # Call graduate class and grab all objects in the class and assign to variable 
    graduate_list = Graduate.objects.all()

    submitted = False

    if request.method == "POST":        
        # Create a form instance from POST data.
        form = GraduateForm(request.POST)
        print(request)
        
        if form.is_valid():
            
            # save a new graduate object from the froms data
            form.save() 
            return HttpResponseRedirect('/manage?submitted=True')
        
    else: 
        form = GraduateForm
        if 'submmitted' in request.GET:
            submitted = True 
    
    # Context Dictionary
    context = { "form":form, 'submitted':submitted, "graduate_list": graduate_list}

    # render takes a request, a template and a payload to pass  
    return render(request, "manage.html", context)

def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")

# delete
def settings(request):
    return render(request, "settings.html")

