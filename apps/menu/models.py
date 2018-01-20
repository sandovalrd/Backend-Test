from django.db import models

# Create your models here.

class AdditionalFood(models.Model):
	"""docstring for Additional"""
	description = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Plastos Extra"

	def __str__(self):
		return self.description

class Food(models.Model):
	"""docstring for Food"""
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=50)
	additional_id = models.ForeignKey(AdditionalFood, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Opciones del Menú"

	def __str__(self):
		return self.name

class Menu(models.Model):
	"""docstring for Menu"""
	name = models.CharField(max_length=20)
	foods = models.ManyToManyField(Food)
	date_menu = models.DateField(auto_now=True)

	class Meta:
		verbose_name = "Menú"

	def __str__(self):
		return self.name
