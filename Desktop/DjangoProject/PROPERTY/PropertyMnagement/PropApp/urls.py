from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    path('tenants/<int:tenant_id>/', views.tenant_detail, name='tenant_detail'),
    path('leases/<int:lease_id>/', views.lease_detail, name='lease_detail'),
]
