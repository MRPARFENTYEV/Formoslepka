from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('all_users/', views.all_users, name='all_users'),
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('edit_user_data/', views.edit_user_data, name='edit_user_data'),
    path('login/', views.user_login, name='user_login'),
    path('admin_delete_users/', views.admin_delete_users, name='admin_delete_users'),
]