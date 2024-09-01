from rest_framework import serializers
from seller.models import ProductInformation



class ProductInformationSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = ProductInformation
        fields ="__all__"


class ProductVerifyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInformation
        fields = ['product_verify']
    

