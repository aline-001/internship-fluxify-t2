from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("properties/", views.property_list),
    path("units/", views.unit_list),
    path("tenants/", views.tenant_list),
    path("leases/", views.lease_list),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('index/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/landlord/', views.landlord_dashboard, name='landlord_dashboard'),
    path('dashboard/tenant/', views.tenant_dashboard, name='tenant_dashboard'),
    path('properties/', views.properties, name='properties'),
    path('tenants/', views.tenants, name='tenants'),
    path('payments/', views.payments, name='payments'),
    path('about/', views.about, name='about'),
    path('add-property/', views.add_property, name='add_property'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name="services"),
    path('property/<int:property_id>/', views.property_details, name='property_details'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

