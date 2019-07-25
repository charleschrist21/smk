from rest_framework import serializers
from .models import siswa

class siswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = siswa
        fields = '__all__'