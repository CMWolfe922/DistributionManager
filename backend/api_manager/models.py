from django.db import models
from django.utils import timezone
from django.core.signing import Signer, TimestampSigner
from datetime import timedelta
import datetime
import zoneinfo

# Cryptographic signer for securing data
signer = TimestampSigner()

# Create your models here.
class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    country_code = models.CharField(max_length=50)
    onsite_instructions = models.CharField(max_length=255)
    location_details = models.CharField(max_length=255)
    
class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer_id = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=100, unique=True)
    customer_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    
class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, related_name='contacts', on_delete=models.CASCADE)
    contact_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_number = models.BigIntegerField(max_length=20)
    mobile_number = models.BigIntegerField(max_length=20)
    email = models.EmailField()

class Pickup(models.Model):
    pickup_id = models.BigAutoField(primary_key=True)
    pu_contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    pu_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    pu_arrival_time = models.DateTimeField()
    pu_depart_time = models.DateTimeField()

class Delivery(models.Model):
    delivery_id = models.BigAutoField(primary_key=True)
    del_contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    del_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    del_arrival_time = models.DateTimeField()
    del_depart_time = models.DateTimeField()

class Order(models.Model):
    TYPE_CHOICES = [
        ('SCHD', "Scheduled"),
        ('CASH', "Cash Customer"),
        ('DIST', "Distribution"),
        ('HTSHOT', "Hot Shot"),
        ('STAT', "Rush Stat"),
        ('ONEHR', "One Hour"),
        ('THRHR', "Three Hour"),
        ('SAMDAY', "Same Day"),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order_pu = models.ForeignKey(Pickup, on_delete=models.SET_NULL, null=True)
    order_del = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True)
    time_placed = models.DateTimeField(auto_now_add=True)
    order_id = models.BigAutoField(primary_key=True, unique_for_date="order_placed")
    order_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    order_complete = models.BooleanField(null=True)
    time_open = models.TimeField(null=True)
    time_to_complete = models.DateTimeField(null=True)
    