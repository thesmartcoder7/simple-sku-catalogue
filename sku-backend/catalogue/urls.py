from django.urls import path
from .views import *

urlpatterns = [
    path('skus/', MedicationSKUAPIView.as_view(), name='sku-list'),
    path('skus/<int:pk>/', MedicationSKUDetailAPIView.as_view(), name='sku-detail'),
]