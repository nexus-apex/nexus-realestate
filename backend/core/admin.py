from django.contrib import admin
from .models import Property, Inquiry, Showing

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "property_type", "location", "area_sqft", "price", "created_at"]
    list_filter = ["property_type", "status"]
    search_fields = ["title", "location"]

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ["client_name", "client_phone", "client_email", "property_title", "inquiry_type", "created_at"]
    list_filter = ["inquiry_type", "status", "source"]
    search_fields = ["client_name", "client_phone", "client_email"]

@admin.register(Showing)
class ShowingAdmin(admin.ModelAdmin):
    list_display = ["property_title", "client_name", "agent", "date", "time_slot", "created_at"]
    list_filter = ["status"]
    search_fields = ["property_title", "client_name", "agent"]
