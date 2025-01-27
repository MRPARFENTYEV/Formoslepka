from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import EditUserForm, MilitaryServiceForm, ContactForm, DiplopmaForm, PassportForm

from accounts.models import User, Military_service
from manager_app.forms import Admin_user_address_data_form


def home_page(request):
    user = request.user
    context = {}
    # if str(user) == 'AnonymousUser':
    # 	return render(request, 'manager_app/home_page.html', context)
    # if user.is_admin:
    # 	return render(request, 'manager_app/home_page.html', context)
    # else:
    return render(request, 'manager_app/home_page.html', context)


def admin_user_address_data(request, user_id):
    user = get_object_or_404(User, id=user_id)
    address = user.adresses.all()
    if address.exists():
        address = address.first()
        form = Admin_user_address_data_form(request.POST or None, instance=address)
    else:

        form = Admin_user_address_data_form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            address = form.save(commit=False)
            address.user = user
            address.save()
            messages.success(request, "Адрес успешно сохранён")
            return render(request, 'accounts/admin_user_address_data.html', {'form': form, 'user': user})

    return render(request, 'accounts/admin_user_address_data.html', {'form': form, 'user': user})


def admin_edit_user_data(request: HttpRequest, user_id: int) -> HttpRequest:
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/edit_user_profile.html', {'form': form, 'user': user})
    else:

        form = EditUserForm(instance=user)

    return render(request, 'accounts/edit_user_profile.html', {'form': form, 'user': user})


def admin_user_military_service_data(request: HttpRequest, user_id: int) -> HttpResponse:
    user = get_object_or_404(User, id=user_id)
    military_service = user.military_service.first()
    form = MilitaryServiceForm(request.POST or None, instance=military_service)

    if request.method == "POST" and form.is_valid():
        military_service = form.save(commit=False)
        military_service.user = user
        military_service.save()
        messages.success(request, "Данные успешно обновлены.")
        return render(request, 'accounts/military_service.html', {'form': form, 'user': user})

    return render(request, 'accounts/military_service.html', {'form': form, 'user': user})



def admin_user_contact(request, user_id):
    user = get_object_or_404(User, id=user_id)
    contacts = user.contacts.first()
    form = ContactForm(request.POST or None, instance=contacts)

    if request.method == "POST" and form.is_valid():
        contacts = form.save(commit=False)
        contacts.user = user
        contacts.save()
        messages.success(request, "Данные успешно обновлены.")
        return render(request, 'accounts/edit_user_contact.html', {'form': form, 'user': user})

    return render(request, 'accounts/edit_user_contact.html', {'form': form, 'user': user})



def admin_user_diploma(request, user_id):
    user = get_object_or_404(User, id=user_id)
    contacts = user.contacts.first()
    form = DiplopmaForm(request.POST or None, instance=contacts)
    if request.method == "POST" and form.is_valid():
        contacts = form.save(commit=False)
        contacts.user = user
        contacts.save()
        messages.success(request, "Данные успешно обновлены.")
        return render(request, 'accounts/edit_user_diploma.html', {'form': form, 'user': user})
    return render(request, 'accounts/edit_user_diploma.html', {'form': form, 'user': user})



def admin_user_passport_data(request, user_id):
    user = get_object_or_404(User, id=user_id)
    passports = user.passports.first()
    form = PassportForm(request.POST or None, instance=passports)
    if request.method == "POST" and form.is_valid():
        passports = form.save(commit=False)
        passports.user = user
        passports.save()
        messages.success(request, "Данные успешно обновлены.")
        return render(request, 'accounts/edit_user_passport.html', {'form': form, 'user': user})
    return render(request, 'accounts/edit_user_passport.html', {'form': form, 'user': user})

