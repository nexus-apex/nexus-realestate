from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Property, Inquiry, Showing
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusRealEstate with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusrealestate.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Property.objects.count() == 0:
            for i in range(10):
                Property.objects.create(
                    title=f"Sample Property {i+1}",
                    property_type=random.choice(["apartment", "villa", "plot", "commercial", "office"]),
                    location=f"Sample {i+1}",
                    area_sqft=random.randint(1, 100),
                    price=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["available", "sold", "rented", "under_construction"]),
                    bedrooms=random.randint(1, 100),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Property records created'))

        if Inquiry.objects.count() == 0:
            for i in range(10):
                Inquiry.objects.create(
                    client_name=f"Sample Inquiry {i+1}",
                    client_phone=f"+91-98765{43210+i}",
                    client_email=f"demo{i+1}@example.com",
                    property_title=f"Sample Inquiry {i+1}",
                    inquiry_type=random.choice(["buy", "rent", "invest"]),
                    budget=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["new", "contacted", "site_visit", "negotiation", "closed"]),
                    source=random.choice(["website", "walk_in", "referral", "portal"]),
                )
            self.stdout.write(self.style.SUCCESS('10 Inquiry records created'))

        if Showing.objects.count() == 0:
            for i in range(10):
                Showing.objects.create(
                    property_title=f"Sample Showing {i+1}",
                    client_name=f"Sample Showing {i+1}",
                    agent=f"Sample {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    time_slot=f"Sample {i+1}",
                    status=random.choice(["scheduled", "completed", "cancelled", "no_show"]),
                    feedback=f"Sample feedback for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Showing records created'))
