from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

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
