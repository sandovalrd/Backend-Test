# Django tools
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
# forms
from .forms import MenuForm, FoodForm, AdditionalForm
# models
from .models import Menu, Food, AdditionalFood
from django.contrib.auth.models import User
# views
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# time
import datetime

# Views for Menu

@login_required()
@permission_required('menu.add_menu')
def menu_create(request):
	"""docstring for menu_create, 
	This view is responsible for creating the corresponding 
	menus of each day"""

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
	"""docstring for MenuUpdate, 
	This view is responsible of editing the menus of each day"""

	model = Menu
	form_class = MenuForm
	success_url = reverse_lazy('menu-list')

class MenuList(LoginRequiredMixin, ListView):
	"""docstring for MenuList, this view shows 
	the last five menus created"""

	queryset = Menu.objects.all()[:5]

def menu_today(request):
	"""docstring for  Menu for today, 
	This view is responsible for showing the daily menu"""

	today = datetime.datetime.now()
	menu_list = Menu.objects.filter(date_menu=today)
	additional_list = AdditionalFood.objects.filter(available=True)
	context = {
		'additional_list': additional_list, 
		'menu_list':menu_list, 
	}
	return render(request, 'menu/menu_today.html', context)

class MunuDetail(DetailView):
	"""docstring for MunuDetail, This view is responsible 
	for displaying the detail of the daily menu and additional meals,
	corresponding to the email link"""

	model = Menu

	def get_context_data(self, **kwargs):
		context = super(MunuDetail, self).get_context_data(**kwargs)
		context['additional_list'] = AdditionalFood.objects.filter(available=True)
		return context
		

# Views for Food

class FoodCreate(LoginRequiredMixin, CreateView):
	"""docstring for FoodCreate, 
	This view is responsible for creating the corresponding 
	foods for menu"""

	model = Food 
	form_class = FoodForm
	success_url = reverse_lazy('food-list')

class FoodUpdate(LoginRequiredMixin, UpdateView):
	"""docstring for FoodUpdate, This view is responsible 
	of editing the corresponding foods for menu"""

	model = Food
	form_class = FoodForm
	success_url = reverse_lazy('food-list')

class FoodList(LoginRequiredMixin, ListView):
	"""docstring for FoodUpdate, This view shows 
	the list of available meals"""

	model = Food

# Views for Additional Food

class AdditionalCreate(LoginRequiredMixin, CreateView):
	"""docstring for AdditionalCreate, 
	This view is responsible for creating the additional food the menu"""

	model = AdditionalFood
	form_class = AdditionalForm
	success_url = reverse_lazy('additional-list')

class AdditionalUpdate(LoginRequiredMixin, UpdateView):
	"""docstring for AdditionalUpdate, 
	This view is responsible of editing the additional food the menu"""

	model = AdditionalFood
	form_class = AdditionalForm
	success_url = reverse_lazy('additional-list')

class AdditionalList(LoginRequiredMixin, ListView):
	"""docstring for AdditionalList, 
	This view is responsible of editing the additional food the menu"""

	model = AdditionalFood

# Views for send email

@login_required()
@permission_required('menu.add_menu')
def send_mail(request):
	"""docstring for send_mail, 
	This view is responsible for sending 
	notifications of the menu by email"""

	menu_today = datetime.datetime.now()
	menu = False
	try:
		# verify that there is not a menu for today
		menu = Menu.objects.get(date_menu=menu_today)
	except:
		pass

	if menu:
		objects_list = User.objects.filter(is_superuser=False)
		subject = 'Cornershop Menu'
		to = []
		for employee in objects_list:
			to.append(employee.email)

		text_content = 'Text'
		html_content = render_to_string(
			'menu/mail_template.html', 
			{'pk': menu.id}
		)

		email = EmailMultiAlternatives(subject, text_content, to=to)
		email.attach_alternative(html_content, "text/html")
		email.send()

		return redirect('menu-today')
	else:
		return render(request, 'menu/menu_today.html')
