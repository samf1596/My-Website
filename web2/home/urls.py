from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from home import views

urlpatterns = [
    path('home/', views.home, name='home'),
]