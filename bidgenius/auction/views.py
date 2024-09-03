from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AuctionDetails
from .serializers import AuctionDetailsSerializer
from django.utils.dateparse import parse_date

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