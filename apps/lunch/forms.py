from django import forms
from .models import Lunch

class LunchForm(forms.ModelForm):

	class Meta:
		model = Lunch
		fields = [
			'employee_id',
			'menu_id',		
			'food_id',
			'additional_food',
			'additional_id',
			'specification',
		]
		labels = {
			'employee_id' : 'Empleado',
			'menu_id' : 'Menu: ',		
			'food_id' : 'Almuerzo: ',
			'additional_food' : 'Comida adicional: ',
			'additional_id' : 'Adicional: ',
			'specification' : 'Observaciones: ',
		}
		widgets = {
			'employee_id' : forms.Select(attrs={'hidden': 'True'}),
			'menu_id' : forms.Select(attrs={'hidden': 'True'}),		
			'food_id' : forms.Select(),
			'additional_food' : forms.CheckboxInput(),
			'additional_id' : forms.Select(),
			'specification' : forms.TextInput(),
		}