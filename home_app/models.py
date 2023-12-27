from django.db import models
from django.db.models import User
# Create your models here.


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True, db_index=True)
    mobile_number = models.CharField(max_length=15, unique=True, blank=True)
    work_number = models.CharField(max_length=15, unique=True, blank=True)
    email = models.EmailField(max_length=200, unique=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Location(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=15)
    description = models.TextField(blank=True, max_length=250, help_text="Description of the location and any notes about the location")
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
class Account(models.Model):
    account_id = models.BigAutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, max_length=250)
    account_contact = models.ForeignKey(Contact, related_name="account_contact", on_delete=models.CASCADE)
    billing_id = models.UUIDField()
    
    
class Driver(models.Model):
    driver_id = models.BigAutoField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_information = models.ManyToManyField(Contact, related_name="contact_info", on_delete=models.CASCADE) 
    license_number = models.IntegerField(unique=True)
    driver_photo = models.ImageField(blank=True, upload_to="/media/images/drivers/<driver_id:int>/")
    vehicle = models.ForeignKey(Vehicle, related_name="vehicle", on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, related_name="active")
    
    def get_open_deliveries(self):
        """Create a methode to return all of the drivers open deliveries"""
        pass
    
    def set_active(self):
        self.__setattr__("active", True)

class Employee(User):
    employee_id = models.BigAutoField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_information = models.ManyToManyField(Contact, related_name="contact_info", on_delete=models.CASCADE) 
    
class Customer(User):
    customer_id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    contact_information = models.ManyToManyField(Contact, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delet=models.CASCADE, description="Customers can have multiple accounts for billing purposes.")
    customer_logo = models.ImageField(upload_to="/media/customer/<customer_id:int>/logo/")
    