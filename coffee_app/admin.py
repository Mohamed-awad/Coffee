from django.contrib import admin
from .models import *


class CoffeeMachinesAdmin(admin.ModelAdmin):
    list_display = ['product_type', 'water_line_compatible', 'code']
    list_per_page = 30


class CoffeePodsAdmin(admin.ModelAdmin):
    list_display = ['product_type', 'coffee_flavor', 'pack_size', 'code']
    list_per_page = 30


admin.site.register(CoffeeMachines, CoffeeMachinesAdmin)
admin.site.register(CoffeePods, CoffeePodsAdmin)
