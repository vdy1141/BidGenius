from django.db import models


class WishList(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name= 'wishlist')
    auctions = models.ForeignKey('auction.AuctionDetails', on_delete=models.CASCADE, related_name='auction_wishlist')


class Transactions(models.Model):
    pass
    
