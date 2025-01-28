<<<<<<< HEAD
# Generated by Django 5.0.7 on 2024-07-15 08:58
=======
# Generated by Django 5.0.7 on 2024-07-17 06:55
>>>>>>> pooja

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='transaction_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_method',
<<<<<<< HEAD
            field=models.CharField(blank=True, choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Wallet', 'Wallet')], max_length=32, null=True),
=======
            field=models.CharField(blank=True, choices=[('Credit Card', 'Credit Card'), ('Debit Crad', 'Debit Card'), ('Wallet', 'Wallet')], max_length=32, null=True),
>>>>>>> pooja
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
