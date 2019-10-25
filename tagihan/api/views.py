from rest_framework import generics


from ..models import tagihan
from ..serializers import tagihanSerializer

class tagihanCreate(generics.ListCreateAPIView):
    queryset = tagihan.objects.all()
    serializer_class = tagihanSerializer

class tagihanDetailAndEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = tagihan.objects.all()
    serializer_class = tagihanSerializer