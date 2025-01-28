from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from seller.views import UserViewSet,ImageViewset
from auction.views import AuctionViewSet
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh
from seller.api import ProductInformationViewsSet,LoginProductInformationViewsSet
from rest_framework.routers import DefaultRouter
from auction.api import AuctionDetailsViewsSet 
from buyer.api import WishListViewSet


router=DefaultRouter()
router.register('products',UserViewSet,basename='products')
router.register('images',ImageViewset,basename='images')
router.register('auction',AuctionViewSet,basename='auction')


router.register('product',ProductInformationViewsSet,basename='product')
router.register('auctiondetails',AuctionDetailsViewsSet,basename='auction')
router.register('login',LoginProductInformationViewsSet, basename='login')
# router.register('wish',WishListViewSet,basename='wish')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/',include(router.urls)),
    path('v1/',include('accounts.urls')),
    path('v1/',include('seller.urls')),
    path('v1/',include('auction.urls')),
    path('access/',token_obtain_pair),
    path('refresh/',token_refresh),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

