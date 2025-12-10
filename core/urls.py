"""
URL configuration for Truong Gia Landing Page.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
]

# Custom error handlers
handler404 = 'landing.views.custom_404'
handler500 = 'landing.views.custom_500'
