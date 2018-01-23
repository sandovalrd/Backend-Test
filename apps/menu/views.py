from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Menu, Food, AdditionalFood
from .forms import MenuForm, FoodForm, AdditionalForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
# Views for Menu

class MenuCreate(CreateView):
	model = Menu 
	form_class = MenuForm
	success_url = reverse_lazy('menu-list')

@login_required()
@permission_required('menu.add_menu')
def menu_create(request):
	if request.method == 'POST': 
		form = MenuForm(request.POST) 
		if form.is_valid(): 
			form.save()
			return redirect('menu-list') 
	else:
		menu_today = datetime.datetime.now()
		try:
			# verify that there is not a menu for today
			menu_list = Menu.objects.filter(date_menu=menu_today)
		except DoesNotExist:
			pass
		form = MenuForm()
		context = {
			'form': form, 
			'menu_list':menu_list, 
		}
	return render(request, 'menu/menu_create_form.html', context)

class MenuUpdate(LoginRequiredMixin, UpdateView):
	model = Menu
	form_class = MenuForm
	success_url = reverse_lazy('menu-list')

class MenuDelete(LoginRequiredMixin, DeleteView):
	model = Menu
	success_url = reverse_lazy('menu-list')

class MenuList(LoginRequiredMixin, ListView):
	# last five registered menus
	queryset = Menu.objects.all()[:5]

def menu_today(request):

	today = datetime.datetime.now()

	menu_list = Menu.objects.filter(date_menu=today)
	additional_list = AdditionalFood.objects.filter(available=True)
	context = {
		'additional_list': additional_list, 
		'menu_list':menu_list, 
	}
	return render(request, 'menu/menu_today.html', context)

# Views for Food

class FoodCreate(LoginRequiredMixin, CreateView):
	model = Food 
	form_class = FoodForm
	success_url = reverse_lazy('food-list')

class FoodUpdate(LoginRequiredMixin, UpdateView):
	model = Food
	form_class = FoodForm
	success_url = reverse_lazy('food-list')

class FoodDelete(LoginRequiredMixin, DeleteView):
	model = Food
	success_url = reverse_lazy('food-list')

class FoodList(LoginRequiredMixin, ListView):
	model = Food

# Views for Additional Food

class AdditionalCreate(LoginRequiredMixin, CreateView):
	model = AdditionalFood
	form_class = AdditionalForm
	success_url = reverse_lazy('additional-list')

class AdditionalUpdate(LoginRequiredMixin, UpdateView):
	model = AdditionalFood
	form_class = AdditionalForm
	success_url = reverse_lazy('additional-list')

class AdditionalDelete(LoginRequiredMixin, DeleteView):
	model = AdditionalFood
	success_url = reverse_lazy('additional-list')

class AdditionalList(LoginRequiredMixin, ListView):
	model = AdditionalFood

