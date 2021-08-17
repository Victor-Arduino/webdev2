from django.forms import ModelForm
from .models import Applicants, result, customUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(ModelForm):
    class Meta:
        model = Applicants
        fields = '__all__'


class ResultForm(ModelForm):
    class Meta:
        model = result
        fields = ['statusOfApplicants']

class CreateUser(UserCreationForm):
    class Meta:
        model = customUser
        fields = ['username', 'email', 'password1', 'password2', 'firstName', 'lastName', 'userType',
                'is_admission', 'is_faculty', 'is_head']

        

        