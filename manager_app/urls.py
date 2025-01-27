from django.shortcuts import render
from django.urls import path
from django.conf.global_settings import DEFAULT_CHARSET
from manager_app import views

app_name = "manager_app"

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('admin_user_address_data/<int:user_id>/', views.admin_user_address_data, name='admin_user_address_data'),
    path('admin_edit_user_data/<int:user_id>/', views.admin_edit_user_data, name='admin_edit_user_data'),
    path('admin_user_military_service_data/<int:user_id>/', views.admin_user_military_service_data, name='admin_user_military_service_data'),
    path('admin_user_contact/<int:user_id>/',views.admin_user_contact, name='admin_user_contact')
]



