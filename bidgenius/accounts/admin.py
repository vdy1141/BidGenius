from django.contrib import admin


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
