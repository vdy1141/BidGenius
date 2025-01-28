# from rest_framework import viewsets, permissions
from buyer.models import WishList
# from .serizalizers import WishListSerializer

# class WishListViewSet(viewsets.ModelViewSet):
#     queryset = WishList.objects.all()
    # serializer_class = WishListSerializer
    #permission_classes = [permissions.IsAuthenticated]


from rest_framework.views import APIView


class WishListViewSet(APIView):
    queryset = WishList.objects.all()