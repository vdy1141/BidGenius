from django.contrib import admin
from .models import AuctionDetails


class AuthionDetailsAdmin(admin.ModelAdmin):
    list_display=["product","auction_id","auction_date","auction_start_time","auction_end_time","increment_amount"]
admin.site.register(AuctionDetails,AuthionDetailsAdmin)