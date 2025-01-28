from django.db import models
from django.utils.timezone import now, timedelta


class ProductCategory(models.Model):
    product_category_id = models.BigAutoField(primary_key=True)
    product_category_name = models.CharField(max_length=30)

    def __str__(self):
<<<<<<< HEAD
        return f"Product Category Id={self.product_category_id} Product Category name={self.product_category_name}"
=======
        return self.product_category_name

>>>>>>> pooja

class ProductInformation(models.Model):

    product_id = models.BigAutoField(primary_key = True)
    product_name = models.CharField(max_length = 30)
    product_description = models.TextField()
    product_manufacture_year = models.PositiveIntegerField(blank= True)
    product_base_price = models.FloatField()
    owner = models.ForeignKey('accounts.User', on_delete = models.CASCADE, related_name = 'products')
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE, related_name='products',blank=True,null=True)
    product_verify = models.BooleanField(default = False)
<<<<<<< HEAD
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, related_name='product_categories',null=True,blank=True)

    def __str__(self):
        return f"Product Id={self.product_id} Product name={self.product_name} product_description={self.product_description} product_base_price={self.product_base_price} owner={self.owner} {self.category}"
    
   
=======


>>>>>>> shivanik

class ProductImages(models.Model):
    product_image = models.ImageField(blank = True, upload_to = 'product_images/')
    product = models.ForeignKey(ProductInformation, on_delete = models.CASCADE, related_name='product_imagess')



