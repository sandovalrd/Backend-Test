from django.contrib import admin
from ..menu.models import Menu, Food, AdditionalFood

# Register your models here.

admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(AdditionalFood)
