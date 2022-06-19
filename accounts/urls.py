from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name = 'index'),
    path('signup/',signup,name = 'signup'),
    path('login/',user_login,name='login'),
    path('login/logout/',user_logout,name='logout'),

]