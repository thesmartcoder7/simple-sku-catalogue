from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MedicationSKU
from .serializers import MedicationSKUSerializer

class MedicationSKUAPIView(APIView):
    def get(self, request):
        skus = MedicationSKU.objects.all()
        serializer = MedicationSKUSerializer(skus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicationSKUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicationSKUDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return MedicationSKU.objects.get(pk=pk)
        except MedicationSKU.DoesNotExist:
            return None

    def get(self, request, pk):
        sku = self.get_object(pk)
        if sku is not None:
            serializer = MedicationSKUSerializer(sku)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        sku = self.get_object(pk)
        if sku is not None:
            serializer = MedicationSKUSerializer(sku, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        sku = self.get_object(pk)
        if sku is not None:
            sku.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)