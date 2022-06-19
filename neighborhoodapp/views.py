from django.shortcuts import render,redirect,get_object_or_404

from .forms import RegisterForm,LoginForm,UserProfileForm,ProfileUpdateForm,HoodForm,PostForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User

from .models import *

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'accounts/register.html',{'form':form})

def login_user(request):
    form = LoginForm()
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('editprofile')
    return render(request, 'accounts/login.html',{'form':form})
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

@login_required(login_url='/login/')
def index(request):
    all_hoods = Neighborhood.objects.all()
    
    return render(request,'index.html',{'all_hoods':all_hoods})

def hood(request):
    if request.method == 'POST':
        form = HoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')
    else:
        form = HoodForm()
    return render(request,'hood.html',{"form":form})

def logout_user(request):
    logout (request)
    return redirect('login')        
        
def join_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood, id=neighborhood_id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('index')

def leave_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighborhood, id=neighborhood_id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('index')

def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')

    else:
        form = PostForm()
    return render(request,'post.html',{"user":current_user,"form":form})