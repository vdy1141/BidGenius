from django.contrib import admin
from .models import AuctionDetails

<<<<<<< HEAD
<<<<<<< HEAD
from . models import AuctionDetails

admin.site.register(AuctionDetails)

# Register your models here.
=======

class AuthionDetailsAdmin(admin.ModelAdmin):
    list_display=["product","auction_id","auction_date","auction_start_time","auction_end_time","increment_amount"]
admin.site.register(AuctionDetails,AuthionDetailsAdmin)
>>>>>>> pooja
=======
@admin.register(AuctionDetails)
class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display = ('auction_id', 'product', 'auction_date', 'auction_start_time', 'auction_end_time', 'increment_amount')
    search_fields = ('auction_id', 'product__id', 'auction_date')

>>>>>>> shivanik
