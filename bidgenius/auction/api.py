from rest_framework import viewsets
from .serizalizers import ProductAuctiomDetailsSerializers
from auction.models import AuctionDetails
from .paginations import AuctionDetailsPagination
from datetime import timedelta
from django.utils import timezone

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


class  AuctionDetailsViewsSet(viewsets.ModelViewSet):
    #serializer_class = AuctionDetailsSerializers
    serializer_class= ProductAuctiomDetailsSerializers
    queryset =AuctionDetails.objects.all().order_by('auction_date') 
    pagination_class = AuctionDetailsPagination
    def get_queryset(self):
        today = timezone.localdate()
        #today = datetime.today().date()
        tomorrow = today + timedelta(days=1)
        print(f"Today's date: {today}")
        print(f"Tomorrow's date: {tomorrow}")
        queryset = AuctionDetails.objects.filter(auction_date__gte=today).order_by('auction_date')
        print(f"Queryset: {queryset}")
        
        return queryset
    

   
     





