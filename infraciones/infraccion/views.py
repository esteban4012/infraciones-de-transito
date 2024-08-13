from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from vehiculo.models import Vehiculo
from .serializers import InfraccionSerializer
from . import serializers
from .models  import Infraccion
from persona.models import Persona


class CargarInfraccionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Extraer la placa del vehículo del cuerpo de la solicitud
        placa_patente = request.data.get('placa_patente')
        
        # Verificar si el vehículo existe
        try:
            vehiculo = Vehiculo.objects.get(placa_del_patente=placa_patente)
        except Vehiculo.DoesNotExist:
            return Response(
                {"error": "El vehículo con la placa proporcionada no existe."},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Si el vehículo existe, proceder a validar y guardar la infracción
        serializer = InfraccionSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except serializers.ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        # Si los datos no son válidos, devolver 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerarInformeAPIView(APIView):
    def get(self, request, email):
        try:
            persona = Persona.objects.get(email=email)
        except Persona.DoesNotExist:
            return Response({"error": "No se encontró una persona con el correo proporcionado."}, status=status.HTTP_404_NOT_FOUND)
        
        infracciones = Infraccion.objects.filter(vehiculo__persona=persona)
        serializer = InfraccionSerializer(infracciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)