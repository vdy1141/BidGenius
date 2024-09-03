from django.db import models
from django.utils.timezone import now, timedelta

class ProductCategory(models.Model):
    product_category_id = models.BigAutoField(primary_key=True)
    product_category_name = models.CharField(max_length=30)


class ProductInformation(models.Model):

    product_id = models.BigAutoField(primary_key = True)
    product_name = models.CharField(max_length = 30)
    product_description = models.TextField()
    product_manufacture_year = models.PositiveIntegerField(blank= True)
    product_base_price = models.FloatField()
    owner = models.ForeignKey('accounts.User', on_delete = models.CASCADE, related_name = 'products')
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE, related_name='products',blank=True,null=True)
    product_verify = models.BooleanField(default = False)



class ProductImages(models.Model):
    product_image = models.ImageField(blank = True, upload_to = 'product_images/')
    product = models.ForeignKey(ProductInformation, on_delete = models.CASCADE, related_name='product_imagess')



