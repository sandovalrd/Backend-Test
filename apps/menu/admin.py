from django.contrib import admin
from ..menu.models import Menu, Food, AdditionalFood

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_menu'
	ordering = ('-date_menu',)
	filter_vertical =  ('foods',)

admin.site.register(Menu, MenuAdmin)
admin.site.register(Food)
admin.site.register(AdditionalFood)
