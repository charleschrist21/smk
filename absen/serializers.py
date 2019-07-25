from rest_framework import serializers
from .models import tanggalAbsen,bulanAbsen

class tanggalSerializer(serializers.ModelSerializer):
    class Meta:
        model = tanggalAbsen
        fields = "__all__"

class bulanSerializer(serializers.ModelSerializer):
    class Meta:
        model = bulanAbsen
        fields = "__all__"