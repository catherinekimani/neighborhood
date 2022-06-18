from django import forms 

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import Profile

class SignupForm(UserCreationForm):
    firstname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','firstname','lastname','email','password1','password2']
        
    def __init__(self,*args,**kwargs):
        super(SignupForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class SigninForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1']
        
    def __init__(self,*args,**kwargs):
        super(SigninForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_bio','user_profile']
        
class ProfileUpdateForm(forms.ModelForm):
    user_bio = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Profile
        fields = ['user_bio','user_contact','user_profile']