from rest_framework import viewsets
from .models import Oficial
from .serializers import OficialSerializer
from rest_framework.permissions import AllowAny

class OficialViewset(viewsets.ModelViewSet):
    queryset = Oficial.objects.all()
    serializer_class = OficialSerializer
    permission_classes = [AllowAny]  # No se requiere autenticación
