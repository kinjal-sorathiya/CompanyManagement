from django import forms
from employee.models import EmployeeModel

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):                                                                            #registration form
    username = forms.EmailField(max_length=8,widget=forms.TextInput(attrs={'placeholder': 'Enter Email Address'}))

    First_name = forms.CharField(required=True,min_length=8)
    Last_name = forms.CharField(required=True)
    Address = forms.CharField(required=True)
    DOB = forms.DateField(required=True)
    Company = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "First_name", "Last_name", "Address", "DOB", "Company")


class LoginForm(forms.Form):                                                                                        #Login Form
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email or Mobile no.'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


class EmployeeForm(forms.ModelForm):                                 #Employee Form
    pass
    class Meta:
        model = EmployeeModel

        fields = '__all__'                                          #what field i required in model

