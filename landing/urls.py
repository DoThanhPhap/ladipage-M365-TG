"""
URL configuration for landing app.
"""
from django.urls import path
from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index, name='index'),
    path('dich-vu/microsoft-365/', views.microsoft365, name='microsoft365'),
    path('dich-vu/van-phong-ao/', views.vanphongao, name='vanphongao'),
    path('dich-vu/chu-ky-so/', views.chukyso, name='chukyso'),
]
