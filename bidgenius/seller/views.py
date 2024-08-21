from django.shortcuts import render
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializers import ProductInfoSerializer,ImageSerializer
from . models import ProductInformation,ProductImages

class UserViewSet(viewsets.ModelViewSet):
    serializer_class=ProductInfoSerializer
    queryset=ProductInformation.objects.all()
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get_queryset(self):
       return super().get_queryset().filter(owner=self.request.user)
     
class ImageViewset(viewsets.ModelViewSet):
    serializer_class=ImageSerializer
    queryset=ProductImages.objects.all()

# Create your views here.
