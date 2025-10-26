from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


MALE_CHOICE='M'
FEMALE_CHOICE='F'
GENDER_CHOICE = [
    ('FEMALE', 'FEMALE'),
    ('MALE', 'MALE'),
    ('OTHER', 'OTHER')
]


class Student(models.Model):
    reg_no=models.CharField(max_length=100, primary_key=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICE)
    email=models.EmailField()
    contact=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    teacher_id=models.CharField(max_length=100, primary_key=True)
    Name=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=100)
    salary=models.IntegerField()
    is_lecture=models.BooleanField()

    def __str__(self):
        return self.Name
