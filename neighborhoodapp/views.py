from django.shortcuts import render,redirect,get_object_or_404

from .forms import RegisterForm,LoginForm,UserProfileForm,ProfileUpdateForm,HoodForm,PostForm,BusinessForm

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
    business = Business.objects.all()
    post = Post.objects.all()
    return render(request,'index.html',{'all_hoods':all_hoods,'business':business,'post':post})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')        
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

@login_required(login_url='/login/')
def hoods(request, neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.neighborhood = neighborhood
            business.user = request.user
            business.save()
            return redirect('index')
    else:
        form = BusinessForm()
        current_user = request.user
        neighborhood = Neighborhood.objects.get(id=neighborhood_id)
        business = Business.objects.filter(neighborhood_id=neighborhood)
        users = Profile.objects.filter(neighborhood=neighborhood)
    return render(request, 'hoods.html', {'form':form, 'form': form, 'users':users,'current_user':current_user, 'neighborhood':neighborhood,'business':business})

@login_required(login_url='/login/')
def post(request,neighborhood_id):
    neighborhood = Neighborhood.objects.get(id=neighborhood_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.neighborhood = neighborhood
            post.user = request.user
            post.save()
            
    else:
        form = PostForm()
        current_user = request.user
        neighborhood = Neighborhood.objects.get(id=neighborhood_id)
        users = Profile.objects.filter(neighborhood=neighborhood)
        post = Post.objects.filter(neighborhood=neighborhood)
    return render(request, 'post.html', {'form':form, 'form': form, 'users':users,'current_user':current_user, 'neighborhood':neighborhood,'post':post})

@login_required(login_url='/login/')
def search_results(request):
    if 'hood_name' in request.GET and request.GET["hood_name"]:
        search_term = request.GET["hood_name"]
        searched_hoods = Neighborhood.search_by_hood_name(search_term)
        message = f"{search_term}"
        print(search_term)
    return render(request, 'search.html',{"message":message,"hoods": searched_hoods})