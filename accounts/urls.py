from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from django.urls import path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('all_users/', views.all_users, name='all_users'),
    path('user_detail/<int:user_id>/', views.user_detail, name='user_detail')

]