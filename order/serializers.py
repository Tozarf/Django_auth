from rest_framework import serializers
from .models import Order_status,Order,Product_detail
from RestaurantData.serializers import RestaurantSerializer
from products.serializers import ProductSerializer
from products.models import Product

class Order_statusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order_status
        fields= ['description'] 

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_detail
        fields= ['quantity']

class OrderSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer()
    status = Order_status()
    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True) 
    products =serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    # quantity = QuantitySerializer()
    class Meta:
        model = Order
        # fields= ['id','user','time','restaurant','status','products','quantity']
        fields= ['id','user','time','restaurant','status','products']

class Product_detailSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True,read_only=True)
    product = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = Product_detail
        fields= ['id','order','product','quantity']




