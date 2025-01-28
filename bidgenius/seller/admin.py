from django.contrib import admin
from . models import ProductInformation,ProductCategory,ProductImages


class ProductImagesAdmin(admin.ModelAdmin):
    display_list=["product_image",]


admin.site.register(ProductInformation,ProductAdmin)
admin.site.register(ProductCategory,CategoryAdmin)
admin.site.register(ProductImages,ProductImagesAdmin)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category_id', 'product_category_name')
    search_fields = ('product_category_name',)


@admin.register(ProductInformation)
class ProductInformationAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_manufacture_year', 'product_base_price', 'product_verify', 'owner', 'product_category')
    list_filter = ('product_verify', 'product_manufacture_year', 'product_category')
    search_fields = ('product_name', 'product_description')
    raw_id_fields = ('owner', 'product_category')

