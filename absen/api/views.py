from rest_framework import generics
from ..models import tanggalAbsen,bulanAbsen
from ..serializers import tanggalSerializer,bulanSerializer

class tanggalAbsenCreate(generics.ListCreateAPIView):
    queryset = tanggalAbsen.objects.all()
    serializer_class = tanggalSerializer

class tanggalAbsenDetailAndEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = tanggalAbsen.objects.all()
    serializer_class = tanggalSerializer

class bulanAbsenCreate(generics.ListCreateAPIView):
    queryset = bulanAbsen.objects.all()
    serializer_class = bulanSerializer

class bulanAbsenCreateDetailAndEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = bulanAbsen.objects.all()
    serializer_class = bulanSerializer