from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', RegPost.as_view(), name = 'registration'),
    path('GetReg/<int:userid>/', GetReg.as_view(), name = 'get reg'),
    path('GetProfile/<int:id>/', GetProfile.as_view(), name = 'get profile'),
    path('profile/', ProfilePost.as_view(), name = 'Profile'),
    path('UserLogin/', UserLogin.as_view(), name = 'UserLogin'),
]
