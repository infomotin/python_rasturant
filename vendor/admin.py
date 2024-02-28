from django.contrib import admin
from vendor.models import vendor
# Register your models here.
class vendorAdmin(admin.ModelAdmin):
    list_display = ('user','vendor_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'vendor_name')
    list_editable = ('is_approved',)
    search_fields = ('vendor_name',)
    list_filter = ('is_approved', 'created_at')



admin.site.register(vendor, vendorAdmin)