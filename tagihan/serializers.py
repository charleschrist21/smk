from rest_framework import serializers
from .models import tagihan

class tagihanSerializer(serializers.ModelSerializer):
    class Meta:
        model = tagihan
        fields = '__all__'