# Django tools
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# forms
from .forms import LunchForm
# models
from .models import Lunch, Menu, AdditionalFood
# time
import datetime, time


@login_required()
def lunch_create(request):
	"""docstring for lunch_create, This view is responsible for 
	creating the employee lunch request"""
	
	if request.method == 'POST': 
		form = LunchForm(request.POST) 
		if form.is_valid(): 
			form.save()
			return redirect('lunch-list') 
	else:
		hour = time.strftime("%H:%M:%S")
		if hour < '11:00:00':
			hour = True
		else:
			hour = False
		menu_today = datetime.datetime.now()
		menu_id=0
		try:
			# only meals from today's menu
			food_list = Menu.objects.filter(date_menu=menu_today)
		except DoesNotExist:
			pass
		if food_list:
			menu_id = Menu.objects.get(date_menu=menu_today)
		# only additional meals that are available
		additional_list = AdditionalFood.objects.filter(available=True) 
		form = LunchForm(initial={'employee_id':request.user.id, 'menu_id': menu_id,})
		context = {
			'form': form, 
			'food_list':food_list, 
			'additional_list': additional_list,
			'hour': hour,
		}
	return render(request, 'lunch/lunch_form.html', context)

@login_required()
def lunch_list(request):
	"""docstring for lunch_list, This view is responsible 
	for showing the last lunch request"""
	
	object_list = Lunch.objects.filter(employee_id_id=request.user.id).order_by('-id')[:1]
	return render(request, 'lunch/lunch_list.html', {'object_list':object_list})

