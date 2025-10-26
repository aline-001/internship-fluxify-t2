from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PropertySerializer, UnitSerializer, TenantSerializer, LeaseSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Sum
from .models import*
from.forms import*
@api_view(['GET', 'POST'])
def property_list(request):
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def property_detail(request, pk):
    try:
        property_instance = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response({'error': 'Property not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertySerializer(property_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PropertySerializer(property_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        property_instance.delete()
        return Response({'message': 'Property deleted'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def unit_list(request):
    if request.method == 'GET':
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def unit_detail(request, pk):
    if request.method == 'GET':
        unit_instance = Unit.objects.get(Unit, pk=pk)
        serializer = UnitSerializer(unit_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        unit_instance = Unit.objects.filter(Unit, pk=pk)
        serializer = UnitSerializer(unit_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        unit_instance = Unit.objects.filter(Unit, pk=pk)
        unit_instance.delete()
        return Response({'message': 'Unit deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def tenant_list(request):
        if request.method == 'GET':
            tenants = Tenant.objects.all()
            serializer = TenantSerializer(tenants, many=True)
            return Response(serializer.data, status= status.HTTP_200_OK)

        elif request.method == 'POST':
            serializer = TenantSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def tenant_detail(request, pk):
        try:
            tenant_instance = Tenant.objects.get(pk=pk)
        except Tenant.DoesNotExist:
            return Response({'error': 'Tenant not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = TenantSerializer(tenant_instance)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TenantSerializer(tenant_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            tenant_instance.delete()
            return Response({'message': 'Tenant deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def lease_list(request):
        if request.method == 'GET':
            leases = Lease.objects.all()
            serializer = LeaseSerializer(leases, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = LeaseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def lease_detail(request, pk):
        try:
            lease_instance = Lease.objects.get(pk=pk)
        except Lease.DoesNotExist:
            return Response({'error': 'Lease not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = LeaseSerializer(lease_instance)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = LeaseSerializer(lease_instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            lease_instance.delete()
            return Response({'message': 'Lease deleted'}, status=status.HTTP_204_NO_CONTENT)



User = get_user_model()

def home(request):
    form = PropertyFilterForm(request.GET)
    properties = Property.objects.all()


    locations = Property.objects.values_list('location', flat=True).distinct()

    if form.is_valid():
        location = form.cleaned_data.get('location')
        if location:
            properties = properties.filter(location=location)
        property_status = form.cleaned_data.get('property_status')
        property_type = form.cleaned_data.get('property_type')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        bedrooms = form.cleaned_data.get('bedrooms')

        if property_status:
            properties = properties.filter(status=property_status)
        if property_type:
            properties = properties.filter(property_type=property_type)
        if min_price:
            properties = properties.filter(price__gte=min_price)
        if max_price:
            properties = properties.filter(price__lte=max_price)
        if bedrooms:
            properties = properties.filter(bedrooms=bedrooms)

    return render(request, 'core/home.html', {'form': form, 'properties': properties, 'locations': locations})



def signin(request):
    if request.user.is_authenticated:
        return redirect_to_dashboard(request.user)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect_to_dashboard(user)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()

    return render(request, 'core/signin.html', {'form': form})

def redirect_to_dashboard(user):
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'landlord':
        return redirect('landlord_dashboard')
    elif user.role == 'tenant':
        return redirect('tenant_dashboard')
    else:
        return redirect('home')
@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'landlord':
        return redirect('landlord_dashboard')
    elif request.user.role == 'tenant':
        return redirect('tenant_dashboard')
    else:
        messages.error(request, "Invalid role. Contact the administrator.")
        return redirect('home')

@login_required
def admin_dashboard(request):
    print(f"User role in admin_dashboard: {request.user.role}")
    total_properties = Property.objects.count()
    total_revenue = Property.objects.filter(status='for-rent').aggregate(Sum('price'))['price__sum'] or 0

    total_rented_properties = Property.objects.filter(status='for-rent', tenant__isnull=False).count()
    occupancy_rate = (total_rented_properties / total_properties) * 100 if total_properties else 0

    recent_maintenance_requests = MaintenanceRequest.objects.order_by('-created_at')[:5]

    active_leases = Lease.objects.filter(is_active=True).count()
    expired_leases = Lease.objects.filter(is_active=False).count()
    total_landlords = User.objects.filter(role='landlord').count()
    total_tenants = User.objects.filter(role='tenant').count()

    chart_data = {
        'labels': ['Total Properties', 'Total Revenue', 'Occupied Properties', 'Available Properties'],
        'data': [total_properties, total_revenue, total_rented_properties, total_properties - total_rented_properties]
    }

    return render(request, 'dashboards/admin_dashboard.html', {
        'total_properties': total_properties,
        'total_revenue': total_revenue,
        'occupancy_rate': occupancy_rate,
        'recent_maintenance_requests': recent_maintenance_requests,
        'active_leases': active_leases,
        'expired_leases': expired_leases,
        'total_landlords': total_landlords,
        'total_tenants': total_tenants,
        'chart_data': chart_data
    })

@login_required
def landlord_dashboard(request):
    properties = Property.objects.filter(owner=request.user)
    active_leases = Lease.objects.filter(property__in=properties, is_active=True)
    tenants = Tenant.objects.filter(property__in=properties)
    chart_data = {
        'labels': ['Total Properties', 'Active Leases', 'Occupied Properties', 'Available Properties'],
        'data': [
            properties.count(),
            active_leases.count(),
            properties.filter(status='Occupied').count(),
            properties.filter(status='Available').count()
        ]
    }

    return render(request, 'dashboards/landlord_dashboard.html', {
        'properties': properties,
        'active_leases': active_leases,
        'tenants': tenants,
        'chart_data': chart_data  # Pass chart data to template
    })

@login_required
def tenant_dashboard(request):
    try:
        tenant = Tenant.objects.get(user=request.user)
        leases = Lease.objects.filter(tenant=tenant)
    except Tenant.DoesNotExist:
        leases = Lease.objects.none()

    # Prepare data for Chart.js
    chart_data = {
        'labels': ['Active Leases', 'Expired Leases'],
        'data': [
            leases.filter(is_active=True).count(),
            leases.filter(is_active=False).count()
        ]
    }

    return render(request, 'dashboards/tenant_dashboard.html', {
        'leases': leases,
        'chart_data': chart_data  # Pass chart data to template
    })

def properties(request):
    return render(request, 'core/properties.html')

def tenants(request):
    return render(request, 'core/tenants.html')

def payments(request):
    return render(request, 'core/payments.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful. You are now logged in!")
            return redirect_to_dashboard(user)
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "you have been logged out!")
    return redirect('signin')

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PropertyForm()
    return render(request, 'core/add_property.html', {'form': form})
def about(request):
    return render(request, 'core/about.html')
from django.shortcuts import render

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

def property_details(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'core/property_details.html', {'property': property})


def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_instance = form.save()
            additional_images = request.FILES.getlist('additional_images')
            for image in additional_images:
                PropertyImage.objects.create(property=property_instance, image=image)

            return redirect('property_detail', pk=property_instance.pk)
    else:
        form = PropertyForm()

    return render(request, 'core/create_property.html', {'form': form})