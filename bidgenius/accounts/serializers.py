from rest_framework import serializers
from .models import User,Country,State,City
from rest_framework import serializers
from .models import Country, State, City
from seller.serializers import ProductInfoSerializer,ProductCategorySerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AccountSerializer(serializers.ModelSerializer):
    product=ProductInfoSerializer(read_only=True,many=True)
    #category=ProductCategorySerializer(read_only=True,many=True)

    role=serializers.HiddenField(default='user')
    class Meta:
        model = User
        fields=['id','password','username','first_name','last_name','email','aadhar_card','pan_card','contact_no','role','product']

    def create(self,validated_data):
         return User.objects.create_user(**validated_data)



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_id', 'country_name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['state_id', 'state_name', 'country']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_id', 'city_name', 'state']

class CustomToken(TokenObtainPairSerializer):
    def validate(self,attrs):
        data =super().validate(attrs)
        obj=self.user
        data['role']=obj.role
        return data