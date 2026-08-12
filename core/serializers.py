from rest_framework import serializers
from .models import Atay

class AtaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Atay
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'available', 'created_at']