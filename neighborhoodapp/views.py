from django.shortcuts import render,redirect

from .forms import SignupForm

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    form = SignupForm()
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request,'accounts/signup.html',{'form':form})