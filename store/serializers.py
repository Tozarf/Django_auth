from rest_framework import serializers
from .models import *
from django.utils.text import gettext_lazy as _
from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError


class StoreSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Store
        fields = ['id','name','address','owner']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id','name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id','name','state','ext_number','int_number']

class EmployeeSerializer(serializers.ModelSerializer):
    job = JobSerializer(many=True, read_only=True)
    home_address = AddressSerializer()

    class Meta:
        model = Employee
        fields = ['id','name','age','last_grade','branch','job','home_address']
        #fields = ['id','name','age','last_grade','job','address']

# class RefreshTokenSerializer(serializers.Serializer):
#     refresh = serializers.CharField()
#     # access = serializers.CharField()

#     default_error_messages = {
#         'bad_token': _('Token is invalid or expired')
#     }

#     def validate(self, attrs):

#         self.refresh_token = attrs['refresh']
#         # self.access_token = attrs['access']
#         return attrs

#     def save(self, **kwargs):
#         try:
#             # AccessToken(self.access_token).blacklist()
#             RefreshToken(self.refresh_token).blacklist()
#         except TokenError:
#             self.fail('bad_token')