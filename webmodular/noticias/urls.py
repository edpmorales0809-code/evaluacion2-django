from django.urls import path
from . import views

urlpatterns = [
    # La ruta vacía '' cargará la lista de noticias
    path('', views.lista_noticias, name='lista_noticias'),
    # La ruta 'info/' cargará la segunda página
    path('info/', views.info_noticias, name='info_noticias'),
]