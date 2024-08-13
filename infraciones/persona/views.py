from rest_framework import viewsets
from .models import Persona
from .serializers import PersonaSerializer
from rest_framework.permissions import AllowAny

class PersonaViewset(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [AllowAny]  # No se requiere autenticación