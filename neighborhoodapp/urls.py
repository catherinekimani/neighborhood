from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    
    path('',views.index,name='index'),
    
    path('hood',views.hood,name='hood')
]