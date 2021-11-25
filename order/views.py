from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer, Order_statusSerializer,Product_detailSerializer
from .models import Order,Order_status,Product_detail

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Order_statusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Order_status.objects.all()
    serializer_class = Order_statusSerializer
    
class Product_detailViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product_detail.objects.all()
    serializer_class = Product_detailSerializer