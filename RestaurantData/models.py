from django.db import models


class Restaurant_type(models.Model):
    description = models.CharField(max_length=50)

    def __str__ (self):
        return self.description


class Direction(models.Model):
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    street = models.CharField(max_length=60)
    int_num = models.IntegerField()
    ext_num = models.IntegerField()
    state = models.CharField(max_length=20)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.city+' '+self.pc+' '+self.street+' '+self.state+' '+self.location

    
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    opening_hour = models.CharField(max_length=80)
    closing_hour = models.CharField(max_length=80)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



