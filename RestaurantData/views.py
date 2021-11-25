from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from .serializers import RestaurantSerializer,Restaurant_typeSerializer,DirectionSerializer
from .models import Restaurant,Restaurant_type,Direction


class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class Restaurant_typeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant_type.objects.all()
    serializer_class = Restaurant_typeSerializer

class DirectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer

