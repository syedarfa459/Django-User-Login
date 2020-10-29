from django.contrib import admin
from django.urls import path
from . import views

app_name = 'userloginsystem'
urlpatterns = [

    path('', views.index, name='home'),
    path('login', views.user_login, name='login'),
]