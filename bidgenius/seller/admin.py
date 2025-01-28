from django.contrib import admin
<<<<<<< HEAD
from . models import ProductInformation,ProductCategory,ProductImages

class ProductAdmin(admin.ModelAdmin):
    display_list=["product_id"," product_name","product_description","product_base_price","owner","category"]

class CategoryAdmin(admin.ModelAdmin):
    display_list=["product_category_id"," product_category_name"]

class ProductImagesAdmin(admin.ModelAdmin):
    display_list=["product_image",]

admin.site.register(ProductInformation,ProductAdmin)
admin.site.register(ProductCategory,CategoryAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)
=======
from .models import ProductCategory,ProductInformation
>>>>>>> pooja

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=["product_category_id","product_category_name"]
admin.site.register(ProductCategory,ProductCategoryAdmin)


class ProductInformationAdmin(admin.ModelAdmin):
    list_display=["product_id","product_name", "product_description" ,"product_manufacture_year","product_base_price","owner","product_category","product_verify"]
admin.site.register(ProductInformation ,ProductInformationAdmin)