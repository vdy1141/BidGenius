from django.urls import path
from .views import CreateAuctionDetailsAPIView,AuctionDetailsByDateAPIView

urlpatterns = [
    path('api/create-auction-details/', CreateAuctionDetailsAPIView.as_view(), name='create-auction-details'),
    path('api/auction/details-by-date/', AuctionDetailsByDateAPIView.as_view(), name='auction-details-by-date'),
]
