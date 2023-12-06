from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from myApp.models import *
from myProject.forms import *


def UserSignupPage(request):
    
    form=UserForm()
    
    if request.method == 'POST':
        
        form=UserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect("SignInPage")
    
    return render(request,'user.html',{'form':form})

def SignInPage(request):
    
    if request.method=='POST':
        form=SignInForm(request.POST)
        
        if form.is_valid():
            
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            user=authenticate(request,username=username,password=password)
            
            if user:
                login(request,user)
                return HttpResponse("Login Successfully")
            else:
                return HttpResponse("Failed")
    else:
        form=SignInForm()
        
        
    return render(request,'signin.html',{'form':form})
                
    