from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

<<<<<<< HEAD

<<<<<<< HEAD
from .models import Country,State,City

class CountryAdmin(admin.ModelAdmin):
    display_list=["country_id","country_name","country_code"]

    

class StateAdmin(admin.ModelAdmin):
    display_list=["state_id","state_name","country"]

    

class CityAdmin(admin.ModelAdmin):
    display_list=["city_id","city_name","state"]



admin.site.register(Country,CountryAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(City,CityAdmin)
# Register your models here.
=======
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'aadhar_card', 'pan_card', 'passport_front', 'passport_back', 'contact_no', 'address', 'city', 'pincode')}),
    )

admin.site.register(User, CustomUserAdmin)
>>>>>>> pooja
=======
class CustomUserAdmin(UserAdmin):
    # Fields to be displayed 
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 
        'role', 'aadhar_card', 'pan_card', 'passport_front', 'passport_back',
        'contact_no', 'address', 'city', 'pincode'
    )
    
    # edit user form
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'role', 'aadhar_card', 'pan_card', 'passport_front', 'passport_back',
            'contact_no', 'address', 'city', 'pincode'
        )}),
    )

admin.site.register(User, CustomUserAdmin)
>>>>>>> shivanik
