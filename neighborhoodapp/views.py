from django.shortcuts import render,redirect

from .forms import SignupForm,SigninForm,UserProfileForm,ProfileUpdateForm,HoodForm

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

def editprofile(request):
    Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST,instance=request.user)
        
        form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        
        if form.is_valid() and form.is_valid():
            
            form.save()
            
            form.save()
            
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
        form = ProfileUpdateForm(instance=request.user.profile)
        
    return render(request,'profile/edit.html',{'form':form})
        
def index(request):
    all_hoods = Neighborhood.objects.all()
    return render(request,'index.html',{"all_hoods":all_hoods})

def hood(request):
    current_user = request.user
    
    if request.method == 'POST':
        form = HoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')
    else:
        form = HoodForm()
    return render(request,'hood.html',{"form":form})
        