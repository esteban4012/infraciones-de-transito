from django.contrib import admin

from .models import Oficial

@admin.register(Oficial)

class OficialAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'numero_identificatorio']
