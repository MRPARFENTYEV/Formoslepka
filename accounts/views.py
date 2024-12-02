from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from accounts.forms import UserRegistrationForm
from accounts.models import User


def paginat(request, list_objects: list):  # https://docs.djangoproject.com/en/5.0/topics/pagination/

    p = Paginator(list_objects, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    return page_obj


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data['email'], data['first_name'], data['last_name'], data['password']
            )
            print(data)
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


def all_users(request):
    users = User.objects.all()
    context = {'users': paginat(request, users)}
    return render(request, 'accounts/all_users.html', context)


def user_detail(request, user_id):
    required_user = User.objects.get(id=user_id)
    user_contacts = required_user.contacts.all()
    user_passports = required_user.passports.all()
    user_addresses = required_user.adresses.all()
    user_diplomas = required_user.diplomas.all()
    user_military_services = required_user.millitary_service.all()

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



