from django.db import models
from django.contrib.auth.models import AbstractUser


## create a user model
class User(AbstractUser):
    pass

    def _str_(self):
        return self.username


property_type = (
    ('Apartment', 'Apartment'),
    ('House', 'House'),
    ('Commercial', 'Commercial'),
    ('Land', 'Land')

)
class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    types = models.CharField(max_length=10, choices=property_type)
    description = models.TextField()
    number_of_units = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.address

class Unit(models.Model):
    property = models.ForeignKey(Property,  null=True, on_delete=models.CASCADE)
    unit_number = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.property.name + " " + str(self.unit_number)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.IntegerField()