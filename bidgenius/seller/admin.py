from django.contrib import admin
from .models import ProductCategory,ProductInformation

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=["product_category_id","product_category_name"]
admin.site.register(ProductCategory,ProductCategoryAdmin)


class ProductInformationAdmin(admin.ModelAdmin):
    list_display=["product_id","product_name", "product_description" ,"product_manufacture_year","product_base_price","owner","product_category","product_verify"]
admin.site.register(ProductInformation ,ProductInformationAdmin)