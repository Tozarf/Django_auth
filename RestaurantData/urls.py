# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'restaurant', views.RestaurantViewSet)
router.register(r'restaurant_type', views.Restaurant_typeViewSet)
router.register(r'direction', views.DirectionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='res_data')),
    
]