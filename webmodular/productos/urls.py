from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MarcaViewSet, ProductoViewSet, VentaViewSet

# Creamos un enrutador que genera automáticamente las URLs RESTful
router = DefaultRouter()
router.register(r'marcas', MarcaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    # --- Rutas de la Evaluación 2 (Tu página web original) ---
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('crear-marca/', views.crear_marca, name='crear_marca'),
    path('modificar-marca/<int:id>/', views.modificar_marca, name='modificar_marca'),
    path('eliminar-marca/<int:id>/', views.eliminar_marca, name='eliminar_marca'),

    path('productos/', views.listar_productos, name='listar_productos'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('modificar-producto/<int:id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('comprar-producto/<int:id>/', views.comprar_producto, name='comprar_producto'),
    
    path('ventas/', views.listar_ventas, name='listar_ventas'),
    path('ventas/crear/', views.crear_venta, name='crear_venta'),
    path('ventas/modificar/<int:id>/', views.modificar_venta, name='modificar_venta'),
    path('ventas/eliminar/<int:id>/', views.eliminar_venta, name='eliminar_venta'),

    # --- Rutas de la Evaluación 3 (Tu nueva API RESTful) ---
    path('api/', include(router.urls)),
]