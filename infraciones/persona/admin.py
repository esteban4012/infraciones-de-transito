from django.contrib import admin

from .models import Persona

@admin.register(Persona)

class AdminPersona(admin.ModelAdmin):
    list_display = ['nombre', 'email']
