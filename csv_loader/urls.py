from django.urls import path
from .views import csv_loader

urlpatterns = [
    path('', csv_loader, name='csv_loader')
]