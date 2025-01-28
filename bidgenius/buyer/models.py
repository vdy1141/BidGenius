from django.db import models


class WishList(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name= 'wishlist')
    auctions = models.ForeignKey('auction.AuctionDetails', on_delete=models.CASCADE, related_name='auction_wishlist')


class Transactions(models.Model):
    CHOICES={
        'Credit Card':'Credit Card',
        'Debit Card':'Debit Card',
        'Wallet':'Wallet'
    }
   # transaction_id=models.BigAutoField(primary_key=True,blank=True)
    transaction_amount=models.FloatField(blank=True,null=True)
    transaction_method=models.CharField(max_length=32,choices=CHOICES ,blank=True,null=True)
    user=models.ForeignKey('accounts.User',on_delete=models.CASCADE ,blank=True,null=True)
    transaction_date= models.DateTimeField(auto_now_add=True ,blank=True,null=True)
    transaction_status=models.CharField(max_length=20 ,blank=True,null=True)
