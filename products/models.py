from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=80)
    price= models.IntegerField()
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)


