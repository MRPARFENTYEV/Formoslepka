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