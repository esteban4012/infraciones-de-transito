from django.db import models

from vehiculo.models import Vehiculo


class Infraccion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    comentarios = models.TextField()

    def __str__(self) -> str:
        return f'{self.vehiculo} - {self.timestamp}'
