from django.db import models

class Oficial(models.Model):
    nombre = models.CharField(max_length=50)
    numero_identificatorio = models.CharField(max_length=20, unique=True, default='DESCONOCIDO')

    def __str__(self) -> str:
        return f'{self.nombre} {self.numero_identificatorio}'