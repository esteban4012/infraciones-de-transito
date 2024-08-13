from rest_framework import viewsets
from .models import Vehiculo
from .serializers import VehiculoSerializer
from rest_framework.permissions import AllowAny

class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [AllowAny]  # No se requiere autenticación