from django.db import models
from django.conf import settings
from ..menu.models import Food, Menu

# Create your models here.

class Lunch(models.Model):
	"""docstring for Lunch"""
	employee_id =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=False)
	menu_id = models.ForeignKey(Menu, on_delete=False)
	food_id = models.ForeignKey(Food, on_delete=False)
	additional_food = models.BooleanField(default=False, verbose_name='Comida Extra')
	date_lunch = models.DateField(auto_now=True)
	specification = models.CharField(max_length=50, blank=True)

	class Meta:
		verbose_name = "Almuerzo"

	def __str__(self):
		return self.food_id.name