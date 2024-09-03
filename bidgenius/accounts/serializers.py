from typing import Any, Dict
from rest_framework import serializers
from .models import User
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ("first_name","last_name","username", "email",
                 "aadhar_card", "pan_card", "passport_front", "passport_back",
                 "contact_no", "address", "city", "pincode")  
        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        obj=self.user
        data['role']=obj.role
        return data     


        
