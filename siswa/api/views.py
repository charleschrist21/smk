from rest_framework import generics
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

from ..models import siswa
from ..serializers import siswaSerializer

class siswaCreate(generics.ListCreateAPIView):
    queryset = siswa.objects.all()
    serializer_class = siswaSerializer

    parser_class = (FileUploadParser)


class siswaDetailAndEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = siswa.objects.all()
    serializer_class = siswaSerializer

    parser_class = (FileUploadParser)