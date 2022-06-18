from django.shortcuts import render,redirect

from .forms import SignupForm,SigninForm,UserProfileForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User

from .models import *

# Create your views here.
def signup(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request,'accounts/signup.html',{'form':form})

def signin(request):
    form = SigninForm()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            
    return render(request,'accounts/signin.html',{'form':form})

def profile(request):
    current_user = request.user
    
    profile = Profile.objects.filter(user_id = current_user.id).first()
    
    return render(request,'profile/profile.html',{"profile":profile})