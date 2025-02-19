from django.db import models
from django.utils.timezone import now  # Import for default time

class CargoRequest(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_surname = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20)
    email = models.EmailField()
    from_country = models.CharField(max_length=100)
    to_country = models.CharField(max_length=100)
    cargo_type = models.CharField(max_length=100)
    description = models.TextField()
    agree_privacy_policy = models.BooleanField(default=False)
    agree_promotions = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ Auto date when created

    def __str__(self):
        return f"{self.company_name} ({self.from_country} → {self.to_country})"
