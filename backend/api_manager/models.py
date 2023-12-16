from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    