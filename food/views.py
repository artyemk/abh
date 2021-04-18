from django.shortcuts import render
from .models import RestaurantInfo
from .models import RestaurantReview
from django.utils import timezone

# Create your views here.

from django.core.files.storage import FileSystemStorage

def thingstodo(request):
    return render(request, "thingstodo.html")

def get_food_places(request):
    rests = RestaurantInfo.objects.filter(active=True)
    reviews_arr = {}
    reviews_count = {}

    for rest in rests:
        reviews = RestaurantReview.objects.filter(unique_id=rest.unique_id).order_by('-pub_date')
        stars = 0
        stars_count = 0
        for review in reviews:
            stars_count += 1
            stars += review.rating 

        try:
            reviews_arr[rest.unique_id] = stars / stars_count
            reviews_count[rest.unique_id] = stars_count
        except ZeroDivisionError:
            reviews_arr[rest.unique_id] = 0
            reviews_count[rest.unique_id] = 0

    context = {
        'rests': rests,
        'reviews_arr' : reviews_arr,
        'reviews_count' : reviews_count
    }
    return render(request, "food.html", context)

def get_food_place(request, id__):
    reviews = RestaurantReview.objects.filter(unique_id=id__).order_by('-pub_date')
    rests = RestaurantInfo.objects.get(unique_id=id__, active=True)
    stars = 0
    stars_count = 0
    rating = 0
    for review in reviews:
        stars_count += 1
        stars += review.rating 

    try:
        rating = stars/stars_count
    except ZeroDivisionError:
        rating = 0

    context = {
        'rest': rests,
        'reviews' : reviews,
        'id__' : id__,
        'stars' : rating,
        'stars_count' : stars_count
    }
    return render(request, "food_one.html", context)

def insert_review(request, id__):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_visit = request.POST.get('date_visit')
        rating = request.POST.get('rating')
        RestaurantReview.objects.create(
            name = name,
            description = description,
            pub_date = timezone.now(),
            date_visit = date_visit,
            rating = rating,
            unique_id = id__
        )

        reviews = RestaurantReview.objects.filter(unique_id=id__).order_by('-pub_date')
        rests = RestaurantInfo.objects.get(unique_id=id__, active=True)

        stars = 0
        stars_count = 0
        rating = 0
        for review in reviews:
            stars_count += 1
            stars += review.rating 

        try:
            rating = stars/stars_count
        except ZeroDivisionError:
            rating = 0



        context = {
            'rest': rests,
            'reviews' : reviews,
            'stars' : rating,
            'id__' : id__,
            'stars_count' : stars_count 
        }
        return render(request, "food_one.html", context)


def insert_rest_tourist(request):
    if request.method == 'POST':

        print(request.POST)

        filename = ""
        name = request.POST.get('place_name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        street = request.POST.get('street')
        street_add = request.POST.get('street_add')
        website = request.POST.get('website')
        price = request.POST.get('price')
        cash = request.POST.get('cash')
        smoke = request.POST.get('smoke')
        wifi = request.POST.get('wifi')

        try:
            if request.FILES['image']:
                myfile = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
        except:
            pass

        if cash == "on":
            cash = True
        else:
            cash = False
        if wifi == "on":
            wifi = True
        else:
            wifi = False
        if smoke == "on":
            smoke = True
        else:
            smoke = False

        cuisine = ""

        for key, _ in request.POST.items():
            if len( key.split("c_") ) > 1:
                if key.split("c_")[1] == "ab":
                    cuisine += "Абхазская, "
                elif key.split("c_")[1] == "az":
                    cuisine += "Азиатская, "
                elif key.split("c_")[1] == "ar":
                    cuisine += "Армянская, "
                elif key.split("c_")[1] == "vt":
                    cuisine += "Вьетнамская, "
                elif key.split("c_")[1] == "gr":
                    cuisine += "Грузинская, "
                elif key.split("c_")[1] == "hl":
                    cuisine += "Здоровая, "
                elif key.split("c_")[1] == "ait":
                    cuisine += "Итальянская, "
                elif key.split("c_")[1] == "kz":
                    cuisine += "Кавказская, "
                elif key.split("c_")[1] == "sh":
                    cuisine += "Суши, "
                elif key.split("c_")[1] == "sf":
                    cuisine += "Морепродукты, "
                elif key.split("c_")[1] == "pz":
                    cuisine += "Пицца, "
                elif key.split("c_")[1] == "ru":
                    cuisine += "Русская, "
                elif key.split("c_")[1] == "uz":
                    cuisine += "Узбекская, "
                elif key.split("c_")[1] == "ul":
                    cuisine += "Уличная еда, "

        RestaurantInfo.objects.create(
            active = False,
            name = name,
            website = website,
            geo = city + " " + street + " " + street_add,
            phone = phone,
            cash = cash,
            wifi = wifi,
            price_group = price,
            smoke = smoke,
            cuisine = cuisine[:-2],
            pricerange = "",
            main_image = filename

        )

        return render(request, "lk.html")