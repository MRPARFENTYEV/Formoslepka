from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import User

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
        # Создаём пустую форму для нового адреса
        form = Admin_user_address_data_form(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            # Сохраняем новый или редактируемый адрес
            address = form.save(commit=False)
            address.user = user  # Привязываем адрес к пользователю
            address.save()
            messages.success(request, "Адрес успешно сохранён")
            return render(request, 'accounts/admin_user_address_data.html', {'form': form, 'user': user})

    return render(request, 'accounts/admin_user_address_data.html', {'form': form, 'user': user})



    #'accounts/register.html'
	# if not hasattr(request.user, 'is_manager'):
	# 	products = Product.objects.filter(avaliable=True)
	# 	context = {'products': paginat(request,products)}  # тут в пагинатор приходит запрос и продукты передаются в виде списка
	# 	return render(request, 'home_page.html', context)
    #
	# if user.is_admin:
	# 	products = Product.objects.all()
	# 	context = {'products': paginat(request ,products)} # тут в пагинатор приходит запрос и продукты передаются в виде списка
	# 	return render(request, 'home_page.html', context)
	# else:
	# 	products = Product.objects.filter(avaliable=True)
	# 	context = {'products': paginat(request,products)}  # тут в пагинатор приходит запрос и продукты передаются в виде списка
	# 	return render(request, 'home_page.html', context)