<<<<<<< HEAD

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import AuctionDetails
from .serializers import AuctionSerializer
from datetime import datetime, timedelta
from .tasks import send_auction_notification

# Schedule email to be sent in 10 minutes
# send_time = datetime.utcnow() + timedelta(minutes=10)
# send_email_task.apply_async(
#     args=['Subject', 'Message', 'from@example.com', ['to@example.com']],
#     eta=send_time
# )


class AuctionViewSet(viewsets.ModelViewSet):
    queryset = AuctionDetails.objects.all()
    serializer_class = AuctionSerializer

    # @action(detail=True, methods=['post'])
    # def register_auction(self, request, pk=None):
    #     auction = self.get_object()
    #     auction.auction_time = request.data.get('auction_start_time')
    #     auction.auction_date = request.data.get('auction_date')
    #     auction.save()

    #     auction_start_time = datetime.combine(auction.auction_date, auction.auction_time)
    #     send_time = auction_start_time - timedelta(hours=1)
    #     subject = f"Auction for {auction.product.product_name} is starting soon"
    #     message = f"Dear {auction.product.owner.username},\n\nYour auction for {auction.product.product_name} is starting on {auction.auction_start_time}."
    #     from_email = 'yog.esh.6g1a9@gmail.com'
    #     recipient_list = [auction.product.owner.email]
    #     print(send_time,recipient_list)


    #     send_auction_notification.apply_async(
    #         args=[subject, message, from_email, recipient_list],
    #         eta=auction_start_datetime
    #     )

=======
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuctionDetails
from .serializers import AuctionDetailsSerializer
from django.utils.dateparse import parse_date
>>>>>>> shivanik

class CreateAuctionDetailsAPIView(APIView):
    def post(self, request):
        serializer = AuctionDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Product added successfully.", 
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)









class AuctionDetailsByDateAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        auctions = AuctionDetails.objects.filter(auction_date__range=[start_date, end_date])
        serializer = AuctionDetailsSerializer(auctions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
















 # if not start_date or not end_date:
        #     return Response({
        #         "error": "Please provide both start_date and end_date parameters."
        #     }, status=status.HTTP_400_BAD_REQUEST)

        # try:
        #     start_date = parse_date(start_date)
        #     end_date = parse_date(end_date)
        # except ValueError:
        #     return Response({
        #         "error": "Invalid date format. Please use YYYY-MM-DD."
        #     }, status=status.HTTP_400_BAD_REQUEST)

        # if start_date > end_date:
        #     return Response({
        #         "error": "Start date must be before or equal to end date."
        #     }, status=status.HTTP_400_BAD_REQUEST)