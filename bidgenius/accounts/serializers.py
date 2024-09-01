# from typing import Any, Dict
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework import serializers
# from .models import User


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
#         data = super().validate(attrs)
#         obj = self.user
#         data['role'] = obj.role
#         return data