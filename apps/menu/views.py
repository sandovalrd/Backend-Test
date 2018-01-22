from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Menu, Food, AdditionalFood
from .forms import MenuForm, FoodForm, AdditionalForm
import datetime
# Views for Menu

class MenuCreate(CreateView):
	model = Menu 
	form_class = MenuForm
	success_url = reverse_lazy('menu-list')

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

class MenuUpdate(UpdateView):
	model = Menu
	form_class = MenuForm
	success_url = reverse_lazy('menu-list')

class MenuDelete(DeleteView):
	model = Menu
	success_url = reverse_lazy('menu-list')

class MenuList(ListView):
	# last five registered menus
	queryset = Menu.objects.all()[:5]

# Views for Food

class FoodCreate(CreateView):
	model = Food 
	form_class = FoodForm
	success_url = reverse_lazy('food-list')

class FoodUpdate(UpdateView):
	model = Food
	form_class = FoodForm
	success_url = reverse_lazy('food-list')

class FoodDelete(DeleteView):
	model = Food
	success_url = reverse_lazy('food-list')

class FoodList(ListView):
	model = Food

# Views for Additional Food

class AdditionalCreate(CreateView):
	model = AdditionalFood
	form_class = AdditionalForm
	success_url = reverse_lazy('additional-list')

class AdditionalUpdate(UpdateView):
	model = AdditionalFood
	form_class = AdditionalForm
	success_url = reverse_lazy('additional-list')

class AdditionalDelete(DeleteView):
	model = AdditionalFood
	success_url = reverse_lazy('additional-list')

class AdditionalList(ListView):
	model = AdditionalFood

