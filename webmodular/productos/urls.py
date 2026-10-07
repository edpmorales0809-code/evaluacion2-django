from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('info/', views.info_productos, name='info_productos'),
    path('ventas/', views.registrar_venta, name='ventas'),
]