from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AbstractUser


# Create your views here.
@api_view(['GET'],['POST'])
def User_list(request):
    if request.method == 'GET'
        Users = AbstractUser.objects.all()
