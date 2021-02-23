from django import forms
from .models import Student
from django.core import validators

class StudentReg(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'password']
        # fields = '__all__'