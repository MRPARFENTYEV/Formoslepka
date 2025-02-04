from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, Page
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import HttpRequest, HttpResponse
from accounts.forms import UserRegistrationForm, UserLoginForm, EditUserForm
from accounts.models import User, Address


def paginat(request: HttpRequest, list_objects: list) -> Page:  # https://docs.djangoproject.com/en/5.0/topics/pagination/

    p = Paginator(list_objects, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj


def user_register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['email'], data['first_name'], data['last_name'], data['password']
            )

            current_site = get_current_site(request)
            # send_mail('Онлайн магазин - Потный айтишник',
            #           f'http://{current_site.domain}/accounts/verify_email/{urlsafe_base64_encode(force_bytes(user.pk))}/{token_generator.make_token(user)}',
            #           EMAIL_HOST_USER, [user.email])
            # confirm_email_notice(request,user)
            context = {'notice': 'Перейдите по ссылке'}
            return render(request, 'accounts/register.html', context)
            # return render(request, 'confirm_email.html', context)
    #
    else:
        form = UserRegistrationForm()
    context = {'title': 'Signup', 'form': form}
    return render(request, 'accounts/register.html', context)

@login_required
def all_users(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    context = {'users': paginat(request, users)}
    return render(request, 'accounts/all_users.html', context)

@login_required
def user_detail(request: HttpRequest, user_id: int) -> HttpResponse:
    required_user = User.objects.get(id=user_id)
    user_contacts = required_user.contacts.all()
    user_passports = required_user.passports.all()
    user_addresses = required_user.adresses.all()
    user_diplomas = required_user.diplomas.all()
    user_military_services = required_user.military_service.all()

    context = {'user_name': required_user.first_name,
               'user_surname': required_user.last_name,
               'user_patronym': required_user.patronym,
               'user_image': required_user.image,
               'user_birthday_date': required_user.birthday_date,
               'user_admin': required_user.is_admin,
               'user_email': required_user.email,
               'user_position': required_user.position,
               'user_contacts': user_contacts,
               'user_passports': user_passports,
               'user_addresses': user_addresses,
               'user_diplomas': user_diplomas,
               'user_military_services': user_military_services}
    return render(request,'accounts/user_detail.html', context)

@login_required
def edit_user_data(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('accounts:user_login')
    print(request.user)
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=request.user)  # Создаём форму с введёнными данными
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профиль был изменен', 'success')
            return redirect('accounts:edit_user_data')
    else:
        form = EditUserForm(instance=request.user)  # Для GET-запроса заполняем форму текущими данными пользователя

    context = {'title': 'Edit Profile', 'form': form}
    return render(request, 'accounts/edit_user_profile.html', context)


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(
                request, email=data['email'], password=data['password']
            )

            if user is not None:

                login(request, user)
                return redirect('manager_app:home_page')
            else:
                messages.error(
                    request, 'Имя или пароль не верны', 'danger'
                )
                return redirect('accounts:user_login')
    else:
        form = UserLoginForm()
    context = {'title':'Login', 'form': form}
    return render(request, 'accounts/login.html', context)
@login_required
def admin_delete_users(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        users_to_delete = request.POST.getlist('users_to_delete')  # Получаем список ID
        User.objects.filter(id__in=users_to_delete).delete()  # Удаляем пользователей
        return redirect('accounts:all_users')  # Перенаправляем на список пользователей
    return redirect('accounts:all_users')







