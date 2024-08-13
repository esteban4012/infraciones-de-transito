from django.db import models
from persona.models import Persona

class Vehiculo(models.Model):
    placa_del_patente = models.CharField(max_length=30, unique=True)
    marca = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.persona.nombre}{self.placa_del_patente}{self.marca}' 


