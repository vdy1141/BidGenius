from django.contrib import admin
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

# Register your models here.
