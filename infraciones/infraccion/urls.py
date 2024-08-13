from django.urls import path
from .views import CargarInfraccionAPIView
from .views import GenerarInformeAPIView

urlpatterns = [
    path('cargar_infraccion/', CargarInfraccionAPIView.as_view(), name='cargar_infraccion'),
    path('generar_informe/<str:email>/', GenerarInformeAPIView.as_view(), name='generar_informe'),
]