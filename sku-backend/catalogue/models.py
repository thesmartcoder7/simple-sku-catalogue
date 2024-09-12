from django.db import models

class MedicationSKU(models.Model):
    medication_name = models.CharField(max_length=255)
    dose = models.CharField(max_length=100)
    presentation = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    countries = models.TextField()

    def __str__(self):
        return f"{self.medication_name} - {self.dose}"
