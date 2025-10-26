from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_landlord(self):
        return self.role == 'landlord'

    @property
    def is_tenant(self):
        return self.role == 'tenant'

class Tenant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()

class Property(models.Model):
    STATUS_CHOICES = [
        ('for-sale', 'For Sale'),
        ('for-rent', 'For Rent'),
    ]

    TYPE_CHOICES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('warehouse', 'Warehouse'),
        ('Land', 'Land'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='for-sale')
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='house')
    location = models.CharField(max_length=100)
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    image = models.ImageField(upload_to='property_images/')
    amenities = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    additional_images = models.ManyToManyField('PropertyImage',
        related_name='properties',
        blank=True
    )
    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def image_gallery(self):
        return self.images.all()

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='property_images/')

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=50)
    is_occupied = models.BooleanField(default=False)

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

class RentPayment(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

from django.db import models

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

class MaintenanceRequest(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='maintenance_requests')
    issue_description = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('resolved', 'Resolved')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Maintenance request for {self.property.title} by {self.tenant.username}"