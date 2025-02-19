from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_1', 'phone_2')  # Display fields in the admin panel
    search_fields = ('username', 'phone_1', 'phone_2')  # Enable search
    list_filter = ('username',)  # Filter messages by email
