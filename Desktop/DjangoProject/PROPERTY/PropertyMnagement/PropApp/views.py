from django.shortcuts import render
from .models import Property, Unit, Tenant, Lease

# View for listing properties
def property_list(request):
    properties = Property.objects.all()
    return render(request, 'properties/property_list.html', {'properties': properties})

# View for a single property details
def property_detail(request, property_id):
    property_obj = Property.objects.get(id=property_id)
    units = Unit.objects.filter(property=property_obj)
    return render(request, 'properties/property_detail.html', {'property': property_obj, 'units': units})

# View for tenant details
def tenant_detail(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    return render(request, 'tenants/tenant_detail.html', {'tenant': tenant})

# View for lease details
def lease_detail(request, lease_id):
    lease = Lease.objects.get(id=lease_id)
    return render(request, 'leases/lease_detail.html', {'lease': lease})
