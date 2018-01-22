from django.urls import path
from .views import lunch_create, lunch_list

urlpatterns = [

    # url for Lunch

    path('add/', lunch_create, name='lunch-add'),
	path('list/', lunch_list, name='lunch-list'),

]