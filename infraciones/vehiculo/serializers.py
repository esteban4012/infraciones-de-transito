from rest_framework import serializers
from .models import Vehiculo
from persona.models import Persona

class VehiculoSerializer(serializers.ModelSerializer):
    persona_nombre = serializers.CharField(source='persona.nombre', read_only=True)
    class Meta:
        model = Vehiculo
        fields = ['id', 'placa_del_patente', 'marca', 'color', 'persona', 'persona_nombre']