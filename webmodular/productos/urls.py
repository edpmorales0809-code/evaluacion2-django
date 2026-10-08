from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Productos
    path('', views.listar_productos, name='listar_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # Rutas para Marcas
    path('marcas/', views.listar_marcas, name='listar_marcas'),
    path('marcas/crear/', views.crear_marca, name='crear_marca'),
    path('marcas/editar/<int:id>/', views.editar_marca, name='editar_marca'),
    path('marcas/eliminar/<int:id>/', views.eliminar_marca, name='eliminar_marca'),
]