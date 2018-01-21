from django.contrib import admin
from ..lunch.models import Lunch

# Register your models here.

class LunchAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_lunch'
	ordering = ('-date_lunch',)

admin.site.register(Lunch, LunchAdmin)
