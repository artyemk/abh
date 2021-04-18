"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views
from food.views import get_food_places, get_food_place, insert_review, insert_rest_tourist, thingstodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('food/', get_food_places, name='get_food_places'),
    path('food/<id__>', get_food_place, name='get_food_place'),
    path('signup/', views.signup, name='signup'),
    path('lk/', views.lk, name='lk'),
    path('add_place/', views.add_place, name='add_place'),
    path('thingstodo/', thingstodo, name='thingstodo'),
    path('insert_rest_tourist/', insert_rest_tourist, name='insert_rest_tourist'),
    path('insert_review/<id__>', insert_review, name='insert_review'),
    path('accounts/', include('django.contrib.auth.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
