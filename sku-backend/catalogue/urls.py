from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('skus/', MedicationSKUAPIView.as_view()),
    path('skus/<int:pk>/', MedicationSKUDetailAPIView.as_view())
]