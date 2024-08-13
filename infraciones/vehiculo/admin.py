from django.contrib import admin

from .models import Vehiculo

@admin.register(Vehiculo)

class AdminVehiculo(admin.ModelAdmin):
    list_display = ['placa_del_patente', 'marca', 'color', 'persona']
    