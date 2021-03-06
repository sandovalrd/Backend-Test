from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class AdditionalFood(models.Model):
	"""docstring for Additional"""
	description = models.CharField(max_length=50)
	available = models.BooleanField(default=True)

	class Meta:
		verbose_name = "Comida Extra"

	def __str__(self):
		return self.description

class Food(models.Model):
	"""docstring for Food"""
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	#additional_id = models.ForeignKey(AdditionalFood, on_delete=False)

	class Meta:
		verbose_name = "Opciones del Menú"

	def __str__(self):
		return self.name

class Menu(models.Model):
	"""docstring for Menu"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=20)
	foods = models.ManyToManyField(Food)
	date_menu = models.DateField(auto_now_add=True)

	class Meta:
		verbose_name = "Menú"
		ordering = ['-date_menu']

	def __str__(self):
		return self.name
