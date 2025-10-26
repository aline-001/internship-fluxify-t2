from django.urls import path
from . import views

urlpatterns = [
    path('accounts/hello', views.say_hello)
]
