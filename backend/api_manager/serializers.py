from rest_framework import serializers
from .models import Order

# CREATE SERIALIZERS FOR EACH MODEL THAT WILL BE USED AS AN BACKEND API

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'first_name', 'last_name', 'order_type']