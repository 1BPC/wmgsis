from django.shortcuts import render
from django.http import HttpResponse
from . import calculate
from . models import Graduate
from . forms import GraduateForm
from django.http import HttpResponseRedirect


def index(request): 
    submitted = False

    if request.method == "POST":        
        # Create a form instance from POST data.
        form = GraduateForm(request.POST)
        print(request)
        
        if form.is_valid():
            
            # save a new graduate object from the froms data
            form.save() 
            return HttpResponseRedirect('/index?submitted=True')
        
    else: 
        form = GraduateForm
        if 'submmitted' in request.GET:
            submitted = True 

    grad_data = calculate.Calculate_Grad()
    degree_class = grad_data.getDegreeClassData()
    salary_data = grad_data.getSalaryData()
    activity = grad_data.getGradActivity()
    
    context = {"grades":degree_class, "city":salary_data, "activity":activity, "form":form, 'submitted':submitted}

    # render takes a request, a template and a payload to pass  
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
   

def manage(request):
    return render(request, "manage.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def settings(request):
    return render(request, "settings.html")

