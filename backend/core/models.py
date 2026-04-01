from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=[("apartment", "Apartment"), ("villa", "Villa"), ("plot", "Plot"), ("commercial", "Commercial"), ("office", "Office")], default="apartment")
    location = models.CharField(max_length=255, blank=True, default="")
    area_sqft = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("available", "Available"), ("sold", "Sold"), ("rented", "Rented"), ("under_construction", "Under Construction")], default="available")
    bedrooms = models.IntegerField(default=0)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Inquiry(models.Model):
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=255, blank=True, default="")
    client_email = models.EmailField(blank=True, default="")
    property_title = models.CharField(max_length=255, blank=True, default="")
    inquiry_type = models.CharField(max_length=50, choices=[("buy", "Buy"), ("rent", "Rent"), ("invest", "Invest")], default="buy")
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("new", "New"), ("contacted", "Contacted"), ("site_visit", "Site Visit"), ("negotiation", "Negotiation"), ("closed", "Closed")], default="new")
    source = models.CharField(max_length=50, choices=[("website", "Website"), ("walk_in", "Walk In"), ("referral", "Referral"), ("portal", "Portal")], default="website")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.client_name

class Showing(models.Model):
    property_title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True, default="")
    agent = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField(null=True, blank=True)
    time_slot = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled"), ("no_show", "No Show")], default="scheduled")
    feedback = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.property_title
