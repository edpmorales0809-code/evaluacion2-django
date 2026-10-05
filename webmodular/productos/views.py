import json
import os
from django.conf import settings
from django.shortcuts import render

# Vista 1: Lee el JSON y muestra el catálogo
def lista_productos(request):
    ruta_json = os.path.join(settings.BASE_DIR, 'data', 'catalogo.json')
    
    with open(ruta_json, 'r', encoding='utf-8') as archivo:
        datos = json.load(archivo)
        
    return render(request, 'productos/lista.html', {'productos': datos})

def info_productos(request):
    return render(request, 'productos/info.html')