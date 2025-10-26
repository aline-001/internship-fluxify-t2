from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Property)
admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(RentPayment)