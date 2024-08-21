
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


# Create your views here.
