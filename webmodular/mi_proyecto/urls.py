from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # <-- 1. Importamos la vista de redirección
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración visual de la página de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Evaluación 3",
        default_version='v1',
        description="Documentación interactiva de la API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    
    # 👇 ESTA ES LA LÍNEA QUE DEBES ASEGURARTE DE AGREGAR 👇
    path('noticias/', include('noticias.urls')), 
    
    # Rutas para ver la documentación de Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    # Redirección de la página principal hacia productos
    path('', RedirectView.as_view(url='/productos/', permanent=True)),
]