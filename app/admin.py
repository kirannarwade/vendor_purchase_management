from django.contrib import admin
from .models import Vendor, PurchaseOrder

# Register your models here.

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_details',
                    'address', 'vendor_code', 
                    'on_time_delivery_rate', 'quality_rating_avg']


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'po_number', 'vendor',
                    'order_date', 'delivery_date', 
                    'items', 'quantity', 'status', 'quality_rating', 'issue_date']
    
