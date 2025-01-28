from rest_framework import serializers
from auction.models import AuctionDetails
from seller.serizalizers import ProductInformationSerializer



class ProductAuctiomDetailsSerializers(serializers.ModelSerializer):
    product= ProductInformationSerializer(read_only=True)

    class Meta:
        model = AuctionDetails
        fields =["product","auction_id","auction_date","auction_start_time","auction_end_time","increment_amount"]