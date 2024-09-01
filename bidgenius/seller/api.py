from rest_framework import viewsets
from .serizalizers import ProductInformationSerializer,ProductVerifyUpdateSerializer
from seller.models import ProductInformation

from django.core.mail import send_mail
from accounts.models import User
from django.conf import settings

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from buyer.models import WishList


from rest_framework.permissions import IsAuthenticated



class ProductInformationViewsSet(viewsets.ModelViewSet):
    serializer_class = ProductInformationSerializer
    queryset= ProductInformation.objects.all()
    

    def perform_create(self, serializer):
        instance = serializer.save()
        #user = self.request.user
        self.send_product_information_email(instance)

    

    def send_product_information_email(self, instance):
        
        subject = f'New Product Information Created By :{instance.owner}'
        message = f'Product Information Details:\n\nName: {instance.product_name}\nDescription: {instance.product_description}\nproduct_manufacture_year:{instance.product_manufacture_year}\nproduct_base_price:{instance.product_base_price}\nowner:{instance.owner}\nproduct_category:{instance.product_category}\nproduct_verify:{instance.product_verify}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [User.objects.get(id=instance.owner_id).email]

        send_mail(subject, message, from_email, recipient_list)

    
    def get_queryset(self):

        queryset = super().get_queryset()
        product_verify =self.request.query_params.get('product_verify')
        if product_verify is not None:
            queryset = queryset.filter(product_verify=product_verify)
        
        return queryset
    


    @action(detail=True, methods=['patch'], url_path='product_verify')
    def update_verify(self, request, pk=None):
        product = self.get_object()
        serializer = ProductVerifyUpdateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            
            send_mail(subject = "Update Information",
            message = f"Product {product.product_verify} verification status has been updated.\n\nProduct Id:{product.product_id}\nProduct Name:{product.product_name}\nDescription: {product.product_description}\nproduct_manufacture_year:{product.product_manufacture_year}\nproduct_base_price:{product.product_base_price}\nowner:{product.owner}\nproduct_category:{product.product_category}\nproduct_verify:{product.product_verify}",
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [User.objects.get(id=product.owner_id).email])
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LoginProductInformationViewsSet(viewsets.ModelViewSet):
   
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset =  ProductInformation.objects.filter(auction__isnull=False)
            return queryset
        return super().get_queryset()
    
    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def add_to_wishlist(self, request, pk=None):
        obj = self.get_object()
        auction = obj.auction
        wishlist = WishList(user=request.user, auctions=auction)
        wishlist.save()
        return Response(data={'detail':'Auction  successfully added to wishlist'}, status=201)

   