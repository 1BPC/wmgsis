from django import forms
from django.forms import ModelForm

from .models import Graduate


# Create a Graduate Form
class GraduateForm(ModelForm):


    class Meta:
        model = Graduate
        fields = ['graduate_name', 'cohort', 'salary', 'city', 'activity', 'degree_classifcation']
        
        labels = {
            'graduate_name': '',
            'cohort': '',
            'salary': '',
            'city': '',
            'activity': '',
            'degree_classifcation': '',
        }

        widgets = {
            'graduate_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'cohort': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cohort Year'}),
            'salary': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Salary'}),
            'city': forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'activity': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Activity'}),
            'degree_classifcation': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Degree Classification'}),
        }

