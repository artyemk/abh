from django.contrib import admin
from food.models import RestaurantInfo

# Register your models here.

class Restaurans(admin.ModelAdmin):
    list_display = ['name', 'description', 'geo', 'phone', 'email', 'cuisine', 'pricerange', 'unique_id'] 

admin.site.register(RestaurantInfo, Restaurans)