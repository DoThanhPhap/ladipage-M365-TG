"""
Views for landing app.
"""
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import ContactForm
from .models import ContactSubmission


def index(request):
    """Landing page view with contact form handling."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Save to database
            ContactSubmission.objects.create(
                name=data['name'],
                phone=data['phone'],
                service=data['service'],
                message=data.get('message', ''),
            )

            # Prepare email content
            service_display = dict(ContactForm.SERVICE_CHOICES).get(data['service'], data['service'])
            subject = f"[Trương Gia] Yêu cầu tư vấn: {service_display}"
            message_body = f"""
Thông tin liên hệ mới:

Họ tên: {data['name']}
Số điện thoại: {data['phone']}
Dịch vụ: {service_display}
Nội dung: {data.get('message') or 'Không có'}
"""
            # Send email notification (optional - may fail if not configured)
            try:
                send_mail(
                    subject=subject,
                    message=message_body,
                    from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', 'noreply@truonggia.vn'),
                    recipient_list=['giaiphaptruonggia@gmail.com'],
                    fail_silently=True,
                )
            except Exception as e:
                # Log error but don't fail (email is secondary, DB is primary)
                print(f"Email send error: {e}")

            messages.success(request, 'Cảm ơn bạn! Chúng tôi sẽ liên hệ trong 24h.')
            return redirect('landing:index')
    else:
        form = ContactForm()

    return render(request, 'landing/index.html', {'form': form})


def microsoft365(request):
    """Microsoft 365 service detail page."""
    return render(request, 'services/microsoft365.html')


def vanphongao(request):
    """Virtual Office service detail page."""
    return render(request, 'services/vanphongao.html')


def chukyso(request):
    """Digital Legal Tools service detail page."""
    return render(request, 'services/chukyso.html')


def custom_404(request, exception):
    """Custom 404 error page."""
    return render(request, 'error_pages/404.html', status=404)


def custom_500(request):
    """Custom 500 error page."""
    return render(request, 'error_pages/500.html', status=500)
