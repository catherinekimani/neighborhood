from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    
    path('profile',views.profile,name='profile'),
    path('editprofile',views.editprofile,name='editprofile'),
    
    path('',views.index,name='index'),
    
    path('hood',views.hood,name='hood'),
    path('join_hood/<neighborhood_id>',views.join_hood,name='join'),
    path('leave_hood/<neighborhood_id>',views.leave_hood,name='leave'),
]