from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('index/', views.index),
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
]