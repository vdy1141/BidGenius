from django.contrib import admin
from .models import AuctionDetails

@admin.register(AuctionDetails)
class AuctionDetailsAdmin(admin.ModelAdmin):
    list_display = ('auction_id', 'product', 'auction_date', 'auction_start_time', 'auction_end_time', 'increment_amount')
    search_fields = ('auction_id', 'product__id', 'auction_date')
