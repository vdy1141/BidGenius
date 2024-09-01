from django.contrib import admin


from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'aadhar_card', 'pan_card', 'passport_front', 'passport_back', 'contact_no', 'address', 'city', 'pincode')}),
    )

admin.site.register(User, CustomUserAdmin)
