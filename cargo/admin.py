from django.contrib import admin
from .models import CargoRequest

@admin.register(CargoRequest)
class CargoRequestAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'from_country', 'to_country', 'cargo_type', 'created_at')  # Fields shown in admin panel
    list_filter = ('from_country', 'to_country', 'cargo_type')  # Filters for easy searching
    search_fields = ('company_name', 'contact_name', 'contact_phone', 'email')  # Searchable fields
    ordering = ('-created_at',)  # Show newest cargo requests first
