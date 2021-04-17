from django.db import models
import uuid

# Create your models here.
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    geo = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    pricerange = models.CharField(max_length=100)
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    main_image = models.ImageField(upload_to='media',default='static/images/pic01.jpg')
    second_image = models.ImageField(upload_to='media',default='static/images/pic01.jpg')
    third_image = models.ImageField(upload_to='media',default='static/images/pic01.jpg')