from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class UserForm(UserCreationForm):
    
    username=forms.CharField(max_length=100, )
    password1=forms.CharField(max_length=100, )
    password2=forms.CharField(max_length=100, )
    
    class Meta:
        model=User
        fields = ['username' , 'password1', 'password2']
        
    
class SignInForm(forms.Form):
    username=forms.CharField(max_length=100, required=False)
    password1=forms.CharField(max_length=100, required=False)
    
    