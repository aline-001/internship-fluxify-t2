from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass


class Profile(models.model):
    User_name = models.Foreignkey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.User_name
