from django import forms
import re
from django.core.exceptions import ValidationError
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields = ['name', 'email', 'course', 'password']
        widgets = {
                'password': forms.PasswordInput(render_value= True )  
            }
        

    def clean_password(self):
            
            password = self.cleaned_data.get('password')
            print("password :   ",password)
            
            
            if not re.search(r'^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$', password):
                raise ValidationError(
                    "Password must be at least 8 characters long, contain at least one uppercase letter, one number, and one special character (e.g., !@#$%^&*)."
                )
            
            return password





