from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer

class MedicationSKUAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sku_data = {
            'medication_name': 'Test Medication',
            'dose': '500mg',
            'presentation': 'Tablet',
            'unit': 'Box of 30',
            'countries': 'Test Country'
        }
        self.sku = MedicationSKU.objects.create(**self.sku_data)

    def test_get_all_skus(self):
        response = self.client.get(reverse('sku-list'))
        skus = MedicationSKU.objects.all()
        serializer = MedicationSKUSerializer(skus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_sku(self):
        new_sku_data = {
            'medication_name': 'New Medication',
            'dose': '250mg',
            'presentation': 'Capsule',
            'unit': 'Bottle of 100',
            'countries': 'New Country'
        }
        response = self.client.post(reverse('sku-list'), new_sku_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MedicationSKU.objects.count(), 2)

    def test_get_single_sku(self):
        response = self.client.get(reverse('sku-detail', kwargs={'pk': self.sku.id}))
        sku = MedicationSKU.objects.get(id=self.sku.id)
        serializer = MedicationSKUSerializer(sku)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_sku(self):
        updated_data = {
            'medication_name': 'Updated Medication',
            'dose': '1000mg',
            'presentation': 'Syrup',
            'unit': 'Bottle of 200ml',
            'countries': 'Updated Country'
        }
        response = self.client.put(
            reverse('sku-detail', kwargs={'pk': self.sku.id}),
            updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_sku = MedicationSKU.objects.get(id=self.sku.id)
        self.assertEqual(updated_sku.medication_name, 'Updated Medication')

    def test_delete_sku(self):
        response = self.client.delete(reverse('sku-detail', kwargs={'pk': self.sku.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MedicationSKU.objects.count(), 0)

    def test_invalid_sku_id(self):
        response = self.client.get(reverse('sku-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)