from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import UserSignup,Userlogin
urlpatterns = [
    
     path('signup/',UserSignup.as_view(),name='signup'),
      path('login/',Userlogin.as_view(),name='login'),
   
]
