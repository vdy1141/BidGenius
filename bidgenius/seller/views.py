
from rest_framework import viewsets
from .models import ProductInformation
from .serializers import ProductInformationSerializer

class ProductInformationViewSet(viewsets.ModelViewSet):
    queryset = ProductInformation.objects.all()
    serializer_class = ProductInformationSerializer
