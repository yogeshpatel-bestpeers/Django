from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

  class Meta:
    model=Student
    fields = ['name', 'email', 'course', 'password']
    widgets = {
            'password': forms.PasswordInput(render_value= True )  
        }



