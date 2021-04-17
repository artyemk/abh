from django.shortcuts import render
from .models import RestaurantInfo

# Create your views here.

def get_food_places(request):
    rests = RestaurantInfo.objects.all()
    context = {
        'rests': rests,
    }
    return render(request, "food.html", context)

def get_food_place(request, id__):
    rests = RestaurantInfo.objects.get(unique_id=id__)
    context = {
        'rest': rests,
    }
    return render(request, "food_one.html", context)