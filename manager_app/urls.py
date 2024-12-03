from django.shortcuts import render
from django.urls import path
from django.conf.global_settings import DEFAULT_CHARSET
from manager_app import views

app_name = "manager_app"

urlpatterns = [
    path('home_page/', views.home_page, name='home_page')]


