from django.contrib import admin
from .models import CustomUser, Property, Unit, Tenant, Lease, RentPayment, Message, MaintenanceRequest

admin.site.register(CustomUser)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(RentPayment)
admin.site.register(Message)
admin.site.register(MaintenanceRequest)
