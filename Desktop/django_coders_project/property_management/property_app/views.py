from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import*

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@staff_member_required
def admin_dashboard(request):
    # Example data to display
    properties = Property.objects.all()
    tenants = Tenant.objects.all()
    context = {
        'properties': properties,
        'tenants': tenants,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
def landlord_dashboard(request):
    properties = Property.objects.filter(owner=request.user.owner)
    return render(request, 'landlord_dashboard.html', {'properties': properties})
@login_required
def tenant_dashboard(request):
    leases = Lease.objects.filter(tenant=request.user.tenant)
    return render(request, 'tenant_dashboard.html', {'leases': leases})

@login_required
def dashboard(request):
    # Example: Display user-specific content based on their role
    user = request.user
    if user.is_staff:
        return render(request, 'admin_dashboard.html')
    elif hasattr(user, 'owner'):
        return render(request, 'landlord_dashboard.html')
    elif hasattr(user, 'tenant'):
        return render(request, 'tenant_dashboard.html')
    else:
        return render(request, 'unknown_role.html')

def property_list(request):
    query = request.GET.get('q', '')
    properties = Property.objects.filter(title__icontains=query) if query else Property.objects.all()
    return render(request, 'property_list.html', {'properties': properties, 'query': query})
def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'property_detail.html', {'property': property})
