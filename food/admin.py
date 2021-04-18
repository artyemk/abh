from django.contrib import admin
from food.models import RestaurantInfo, RestaurantReview

# Register your models here.

class Restaurans(admin.ModelAdmin):
    list_display = ['active', 'name', 'geo', 'phone', 'cuisine', 'unique_id'] 

admin.site.register(RestaurantInfo, Restaurans)

class RestaurantsReview(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_visit', 'rating'] 

admin.site.register(RestaurantReview, RestaurantsReview)