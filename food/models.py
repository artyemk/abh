from django.db import models
import uuid
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class RestaurantInfo(models.Model):
    active = models.BooleanField(default=False)
    cash = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    smoke = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100, default="")
    price_group = models.CharField(max_length=100, default="")
    geo = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    cuisine = models.CharField(max_length=100)
    pricerange = models.CharField(max_length=100, blank=True)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    main_image = models.ImageField(upload_to='media',default='static/images/pic01.jpg')
    second_image = models.ImageField(upload_to='media',default='static/images/pic01.jpg')
    third_image = models.ImageField(upload_to='media',default='static/images/pic01.jpg')

class RestaurantReview(models.Model):
    unique_id = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, default="")
    pub_date = models.DateTimeField('date published')
    date_visit = models.CharField(max_length=100)
    rating = IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
     )