from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import infraccion
from persona.views import PersonaViewset
from vehiculo.views import VehiculoViewset
from oficial.views import OficialViewset
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'persona', PersonaViewset)
router.register(r'vehiculo', VehiculoViewset)
router.register(r'oficial', OficialViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('infracciones/', include('infraccion.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
