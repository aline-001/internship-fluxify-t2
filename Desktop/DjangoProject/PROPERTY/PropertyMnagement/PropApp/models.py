from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

class Property(models.Model):
    STATUS_CHOICES = [
        ('for-sale', 'For Sale'),
        ('for-rent', 'For Rent'),
    ]

    TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('warehouse', 'Warehouse'),
    ]

    title = models.CharField(max_length=200,default='Title')
    description = models.TextField(default='Description')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='for-sale')
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='house')
    location = models.CharField(max_length=100, default='no location specified')
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    image = models.ImageField(upload_to='property_images/', default='default.jpg')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=50)
    is_occupied = models.BooleanField(default=False)

class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('expired', 'Expired')])


class RentPayment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('bank_transfer', 'Bank Transfer'), ('cash', 'Cash')])

