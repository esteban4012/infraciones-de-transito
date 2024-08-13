from django.contrib import admin

from .models import Infraccion

@admin.register(Infraccion)

class InfraccionAdmin(admin.ModelAdmin):
    list_display = ['vehiculo','timestamp','comentarios']
