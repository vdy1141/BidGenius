

from celery import shared_task
from . models import AuctionDetails
from datetime import date
from time import sleep
from django.core.mail import send_mail

@shared_task
def send_auction_notification():
    current_date=date.today()
    auctions=AuctionDetails.objects.filter(auction_date=current_date)
    for auction in auctions:
        subject = f"Auction for {auction.product.product_name} is starting soon"
        message = f"Dear {auction.product.owner.username},\n\nYour auction for {auction.product.product_name} is starting on {auction.auction_start_time}."
        from_email = 'yog.esh.6g1a9@gmail.com'
        recipient_list = [auction.product.owner.email]
        send_mail(subject, message, from_email, recipient_list)