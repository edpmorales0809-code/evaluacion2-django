from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Enrutador para los ViewSets de la API REST (Esto es lo que alimenta a Swagger)
router = DefaultRouter()
router.register(r'api/marcas', views.MarcaViewSet, basename='api-marca')
router.register(r'api/productos', views.ProductoViewSet, basename='api-producto')
router.register(r'api/ventas', views.VentaViewSet, basename='api-venta')

urlpatterns = [
    # --- RUTAS WEB (HTML) ---
    path('', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marcas/crear/', views.crear_marca, name='crear_marca'),
    path('marcas/editar/<int:id>/', views.editar_marca, name='editar_marca'),
    path('marcas/eliminar/<int:id>/', views.eliminar_marca, name='eliminar_marca'),

    # --- RUTAS DE LA API (DRF) ---
    path('', include(router.urls)),
]