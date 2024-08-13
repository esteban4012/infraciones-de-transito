from rest_framework import serializers
from .models import Oficial

class OficialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oficial
        fields = '__all__'
