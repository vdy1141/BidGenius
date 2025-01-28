<<<<<<< HEAD
from . models import ProductInformation,ProductCategory,ProductImages
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields='__all__'



class ProductCategorySerializer(serializers.ModelSerializer):
   class Meta:
      model=ProductCategory
      fields='__all__'

class ProductInfoSerializer(serializers.ModelSerializer):
   product_imagess = ImageSerializer(many=True, read_only=True)
   category =ProductCategorySerializer(read_only=True)
   owner= serializers.HiddenField(default=serializers.CurrentUserDefault())
   class Meta:
        model=ProductInformation
       # fields='__all__'
        fields=['product_id','product_name','product_description','product_manufacture_year','product_base_price','category','owner','product_imagess']
=======
from rest_framework import serializers
from seller.models import ProductInformation

class ProductInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInformation
        fields = '__all__'
>>>>>>> shivanik
