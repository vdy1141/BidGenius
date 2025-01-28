from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductInformationViewSet

router = DefaultRouter()
router.register(r'products', ProductInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

