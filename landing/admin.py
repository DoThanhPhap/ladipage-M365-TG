"""
Admin configuration for landing app.
"""
import os
from django.contrib import admin

# Only register admin if not on Vercel (no database on serverless)
IS_VERCEL = os.environ.get('VERCEL', False)

if not IS_VERCEL:
    from .models import ContactSubmission

    @admin.register(ContactSubmission)
    class ContactSubmissionAdmin(admin.ModelAdmin):
        """Admin interface for contact submissions."""

        list_display = ['name', 'phone', 'service', 'status', 'created_at']
        list_filter = ['status', 'service', 'created_at']
        search_fields = ['name', 'phone', 'message']
        list_editable = ['status']
        readonly_fields = ['created_at', 'updated_at']
        ordering = ['-created_at']

        fieldsets = (
            ('Thông tin khách hàng', {
                'fields': ('name', 'phone', 'service', 'message')
            }),
            ('Quản lý', {
                'fields': ('status', 'notes')
            }),
            ('Thời gian', {
                'fields': ('created_at', 'updated_at'),
                'classes': ('collapse',)
            }),
        )


# Customize admin site header
admin.site.site_header = 'Tự Động Hoá Trương Gia - Admin'
admin.site.site_title = 'Trương Gia Admin'
admin.site.index_title = 'Quản lý hệ thống'
