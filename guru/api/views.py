from rest_framework import generics
from rest_framework.parsers import FileUploadParser

from ..models import Guru
from ..serializers import GuruSerializer

class GuruCreate(generics.ListCreateAPIView):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer
    parser_class = (FileUploadParser)

class guruDetailAndEdit(generics.ListCreateAPIView):
    queryset = Guru.objects.all()
    serializer_class = GuruSerializer
    parser_class = (FileUploadParser)