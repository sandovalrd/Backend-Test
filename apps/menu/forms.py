from django import forms
from .models import Menu, Food, AdditionalFood

class MenuForm(forms.ModelForm):

	class Meta:
		model = Menu
		fields = [
			'name',
			'foods',		]
		labels = {
			'name' : 'Nombre del Menú: ',
			'foods' : 'Comidas disponibles: ',
		}
		widgets = {
			'name' : forms.TextInput(),
			'foods' : forms.CheckboxSelectMultiple(),
		}

class FoodForm(forms.ModelForm):

	class Meta:
		model = Food
		fields = [
			'name',
			'description',
		]
		labels = {
			'name' : 'Nombre de la Comida: ',
			'description' : 'Descripcion de la comida: ',
		}
		widgets = {
			'name' : forms.TextInput(),
			'description' : forms.Textarea(),
		}

class AdditionalForm(forms.ModelForm):

	class Meta:
		model = AdditionalFood
		fields = [
			'description',
			'available',
		]
		labels = {
			'description' : 'Nombre de la Comida: ',
			'available' : 'disponible: ',
		}
		widgets = {
			'description' : forms.TextInput(),
			'available' : forms.CheckboxInput(),
		}