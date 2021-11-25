from rest_framework import serializers

from .models import Restaurant_type,Restaurant,Direction


class Restaurant_typeSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Restaurant_type
        fields = ['description']

class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Direction
        fields = ['id','city','zip_code','street','int_num','ext_num','state','location']

class RestaurantSerializer(serializers.ModelSerializer):
    direction= DirectionSerializer()
    restaurant = Restaurant_typeSerializer()
    class Meta:
        model = Restaurant
        fields = ['id', 'name','opening_hour','closing_hour','direction','phone','restaurant']