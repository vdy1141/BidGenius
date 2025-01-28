<<<<<<< HEAD
from . models import AuctionDetails
from rest_framework import serializers

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuctionDetails
        fields='__all__'
=======
from rest_framework import serializers
from .models import AuctionDetails
from django.utils import timezone
from datetime import timedelta

class AuctionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionDetails
        fields = ['product', 'auction_id', 'auction_date', 'auction_start_time', 'auction_end_time', 'increment_amount']

    def validate(self, data):
        # Perform custom validation here
        auction_date = data.get('auction_date')
        auction_start_time = data.get('auction_start_time')
        auction_end_time = data.get('auction_end_time')
        increment_amount = data.get('increment_amount')
        
        current_date = timezone.now().date()
        min_auction_date = current_date + timedelta(days=7)

        if auction_date:
            if auction_date < min_auction_date:
                raise serializers.ValidationError(f"Auction date must be at least 7 days from today. Minimum date is {min_auction_date}.")
        
        if auction_start_time and auction_end_time:
            if auction_end_time <= auction_start_time:
                raise serializers.ValidationError("Auction end time must be after the start time.")
                
        if increment_amount is not None and increment_amount <= 0:
            raise serializers.ValidationError("Increment amount must be positive.")
        
        return data
>>>>>>> shivanik
