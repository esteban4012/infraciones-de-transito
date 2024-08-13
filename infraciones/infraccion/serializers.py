from rest_framework import serializers
from .models import Infraccion
from vehiculo.models import Vehiculo
from rest_framework.exceptions import ValidationError
from vehiculo.serializers import VehiculoSerializer

class InfraccionSerializer(serializers.ModelSerializer):
    placa_patente = serializers.CharField(write_only=True)
    vehiculo = VehiculoSerializer(read_only=True)  

    class Meta:
        model = Infraccion
        fields = ['placa_patente', 'timestamp', 'comentarios', 'vehiculo']

    def create(self, validated_data):
        placa_patente = validated_data.pop('placa_patente')
        try:
            vehiculo = Vehiculo.objects.get(placa_del_patente=placa_patente)
        except Vehiculo.DoesNotExist:
            raise ValidationError("No se encontró un vehículo con la placa proporcionada.")
        except Vehiculo.MultipleObjectsReturned:
            raise ValidationError("Se encontraron múltiples vehículos con la misma placa. Verifica la base de datos.")
        return Infraccion.objects.create(vehiculo=vehiculo, **validated_data)

