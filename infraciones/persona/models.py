from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.nombre
