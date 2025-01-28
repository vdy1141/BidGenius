# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from django.utils.timezone import now, timedelta
# from .models import ProductInformation
# from auction.models import AuctionDetails
# from .serializers import ProductInformationSerializer

# class ProductInformationViewSet(viewsets.ModelViewSet):
#     queryset = ProductInformation.objects.all()
#     serializer_class = ProductInformationSerializer

#     def create(self, request, *args, **kwargs):
#         response = super().create(request, *args, **kwargs)
#         product = ProductInformation.objects.get(pk=response.data['product_id'])
#         auction_date = now().date() + timedelta(days=7)
#         # auction_start_time = now().time()
#         # auction_end_time = (now() + timedelta(hours=2)).time()  # Assuming the auction lasts for 2 hours
#         AuctionDetails.objects.create(
#             product=product,
#             auction_date=auction_date,
#             # auction_start_time=auction_start_time,
#             # auction_end_time=auction_end_time,
#             # increment_amount=100.0  # Assuming a default increment amount
#         )
        
#         response.data['auction_date'] = auction_date
#         # response.data['auction_start_time'] = auction_start_time
#         # response.data['auction_end_time'] = auction_end_time
#         return response