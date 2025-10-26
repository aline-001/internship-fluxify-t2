from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your model
class User(AbstractUser):
    pass
    def __str__(self):
        return self.email

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user
class Product(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order =models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.user