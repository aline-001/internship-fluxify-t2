from django.contrib import admin
from .models import User, Owner, Property, Unit, Tenant, Lease, RentPayment


admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Property)
admin.site.register(Unit)
admin.site.register(Tenant)
admin.site.register(Lease)
admin.site.register(RentPayment)
