"""
Models for landing app.
"""
from django.db import models


class ContactSubmission(models.Model):
    """Store contact form submissions."""

    SERVICE_CHOICES = [
        ('m365', 'Microsoft 365'),
        ('office', 'Văn phòng ảo'),
        ('digital', 'Chữ ký số & Hoá đơn'),
        ('all', 'Tất cả dịch vụ'),
    ]

    STATUS_CHOICES = [
        ('new', 'Mới'),
        ('contacted', 'Đã liên hệ'),
        ('converted', 'Đã chuyển đổi'),
        ('closed', 'Đã đóng'),
    ]

    name = models.CharField('Họ tên', max_length=100)
    phone = models.CharField('Số điện thoại', max_length=15)
    service = models.CharField('Dịch vụ', max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField('Nội dung', blank=True)
    status = models.CharField('Trạng thái', max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField('Ghi chú', blank=True, help_text='Ghi chú nội bộ')
    created_at = models.DateTimeField('Ngày tạo', auto_now_add=True)
    updated_at = models.DateTimeField('Cập nhật', auto_now=True)

    class Meta:
        verbose_name = 'Yêu cầu tư vấn'
        verbose_name_plural = 'Yêu cầu tư vấn'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.get_service_display()})"
