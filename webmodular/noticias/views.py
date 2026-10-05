import json
import os
from django.conf import settings
from django.shortcuts import render

# Vista 1: Lee el JSON y muestra las noticias
def lista_noticias(request):
    # Apuntamos a la carpeta 'data' donde está nuestro archivo
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'articulos.json')
    
    # Abrimos y leemos el archivo JSON
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        
    # Enviamos los datos a la plantilla HTML a través de un diccionario
    return render(request, 'noticias/lista.html', {'noticias': datos})

def info_noticias(request):
    return render(request, 'noticias/info.html')