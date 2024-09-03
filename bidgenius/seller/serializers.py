from rest_framework import serializers
from seller.models import ProductInformation

class ProductInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInformation
        fields = '__all__'
