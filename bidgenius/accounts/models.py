from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Country(models.Model):
    country_id = models.BigAutoField(primary_key = True)
    country_name = models.CharField(max_length = 30)
    country_code = models.CharField(max_length = 5)

    def __str__(self):
        return f"Country={self.country_name},Code={self.country_code}"

    
class State(models.Model):
    state_id = models.BigAutoField(primary_key = True)
    state_name = models.CharField(max_length = 30)
    country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name= 'states')

    def __str__(self):
        return f"State={self.state_name},{self.country}"

    
class City(models.Model):
    city_id = models.BigAutoField(primary_key = True)
    city_name = models.CharField(max_length = 30)
    state = models.ForeignKey(State, on_delete = models.CASCADE, related_name= 'cities')

    def __str__(self) -> str:
        return f'City={self.city_name},{self.state}'

    
class User(AbstractUser):
    CHOICES = [('user', 'user'),('admin', 'admin')]
    role = models.CharField(max_length=5,choices=CHOICES)
    aadhar_card = models.ImageField(blank=True, upload_to='aadhar/')
    pan_card = models.ImageField(blank=True, upload_to='pan_card/')
    passport_front = models.ImageField(blank=True, upload_to='passport_front/')
    passport_back = models.ImageField(blank=True, upload_to='passport_back/')
    contact_no = PhoneNumberField(blank=True, region='IN')
    address = models.TextField(blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='users', blank=True, null=True)
    pincode = models.PositiveIntegerField(blank=True, null=True)

        
class BankInformation(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=20)
    bank_address = models.TextField()
    bank_account_number = models.CharField(max_length=20, unique=True)
    branch_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bank_details')


class FeedBack(models.Model):
    email = models.EmailField()
    response = models.TextField()
    feedback_date = models.DateTimeField(auto_now_add=True)
