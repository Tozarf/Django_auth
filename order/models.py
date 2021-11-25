from django.db import models
# Create your models here.
from django.conf import settings
from products.models import Product
from users.models import User
from RestaurantData.models import Restaurant
# from products.models import Product

class Order_status(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Order_status, null=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through= "Product_detail")

    def __str__(self):
        return self.user.username

class Product_detail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    
    

