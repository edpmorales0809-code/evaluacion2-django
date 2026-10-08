from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto, Venta
from .forms import MarcaForm, ProductoForm
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import (
    MarcaSerializer, 
    ProductoAdminSerializer, 
    ProductoPublicoSerializer, 
    VentaSerializer
)

# --- MANTENEDOR DE MARCAS (CRUD) ---

@login_required
def listar_marcas(request):
    buscar = request.GET.get('buscar')
    if buscar:
        marcas = Marca.objects.filter(nombre__icontains=buscar)
    else:
        marcas = Marca.objects.all()
    return render(request, 'producto/listar_marcas.html', {'marcas': marcas})

@login_required
def crear_marca(request):
    if request.method == 'POST':
        formulario = MarcaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_marcas')
    else:
        formulario = MarcaForm()
    return render(request, 'producto/form_marca.html', {'form': formulario})

@login_required
def editar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_marcas')
    else:
        formulario = MarcaForm(instance=marca)
    return render(request, 'producto/form_marca.html', {'form': formulario})

@login_required
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('listar_marcas')

# --- MANTENEDOR DE PRODUCTOS (CRUD) ---

@login_required
def listar_productos(request):
    buscar = request.GET.get('buscar')
    if buscar:
        productos = Producto.objects.filter(nombre__icontains=buscar)
    else:
        productos = Producto.objects.all()
    return render(request, 'producto/listar_productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm()
    return render(request, 'producto/form_producto.html', {'form': formulario})

@login_required
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'producto/form_producto.html', {'form': producto})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')

# --- VISTAS DE API REST (DRF) ---

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.user and self.request.user.is_staff:
            return ProductoAdminSerializer
        return ProductoPublicoSerializer

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]