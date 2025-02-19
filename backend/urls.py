from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('my_app.urls')),
    path('api1/', include('authapp.urls')),  # Include authapp URLs
    path('api2/', include('cargo.urls')),  # Include authapp URLs
    path('api3/', include('contacts.urls')),  # Include authapp URLs
    path('api4/', include('messages_api.urls')),  # Include authapp URLs
]
