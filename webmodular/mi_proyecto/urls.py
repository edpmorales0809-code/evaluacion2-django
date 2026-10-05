from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

# Pequeña función para redirigir la página de inicio directamente a las noticias
def inicio(request):
    return redirect('/noticias/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'), # Actúa como punto de entrada
    path('noticias/', include('noticias.urls')), # Vincula la app noticias
    path('productos/', include('productos.urls')), # Vincula la app productos
]