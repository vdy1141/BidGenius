from . models import AuctionDetails
from rest_framework import serializers

class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuctionDetails
        fields='__all__'