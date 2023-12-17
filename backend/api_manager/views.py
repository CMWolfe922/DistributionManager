from django.shortcuts import render
from rest_framework import viewsets
from .models import Order, Customer, Contact, Location, Pickup, Delivery, Driver
from .serializers import OrderSerializer, CustomerSerializer, ContactSerializer
from .serializers import LocationSerializer, PickupSerializer, DeliverySerializer, DriverSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class PickupViewSet(viewsets.ModelViewSet):
    queryset = Pickup.objects.all()
    serializer_class = PickupSerializer
    
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    
class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer