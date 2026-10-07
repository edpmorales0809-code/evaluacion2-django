<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Marca, Producto, Venta
from .forms import MarcaForm, ProductoForm, VentaForm

# --- MANTENEDOR DE MARCAS (CRUD) ---

# 1. Leer (Listar)
@login_required
def listar_marcas(request):
    buscar = request.GET.get('buscar')
    
    if buscar:
        # Filtra las marcas por nombre
        marcas = Marca.objects.filter(nombre__icontains=buscar)
    else:
        marcas = Marca.objects.all()

    return render(request, 'producto/listar_marcas.html', {'marcas': marcas})

# 2. Crear
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

# 3. Actualizar (Modificar)
@login_required
def modificar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    if request.method == 'POST':
        formulario = MarcaForm(data=request.POST, instance=marca)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_marcas')
    else:
        formulario = MarcaForm(instance=marca)
    return render(request, 'producto/form_marca.html', {'form': formulario})

# 4. Eliminar
@login_required
def eliminar_marca(request, id):
    marca = get_object_or_404(Marca, id=id)
    marca.delete()
    return redirect('listar_marcas')

# --- MANTENEDOR DE PRODUCTOS (CRUD) ---

@login_required
def listar_productos(request):
    # Capturamos lo que el usuario escribe en el buscador
    buscar = request.GET.get('buscar')
    
    if buscar:
        # Filtra los productos cuyo nombre contenga el texto buscado
        productos = Producto.objects.filter(nombre__icontains=buscar)
    else:
        # Si no busca nada, muestra todos
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
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_productos')
    else:
        formulario = ProductoForm(instance=producto)
    return render(request, 'producto/form_producto.html', {'form': formulario})

@login_required
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')

# --- LA TRANSACCIÓN (COMPRAR Y DESCONTAR STOCK) ---
@login_required
def comprar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    # Valida que haya stock antes de descontar
    if producto.stock > 0:
        producto.stock -= 1
        producto.save()
    return redirect('listar_productos')

@login_required
def listar_ventas(request):
    ventas = Venta.objects.all()
    # Buscador opcional
    buscar = request.GET.get('buscar')
    if buscar:
        ventas = ventas.filter(producto__nombre__icontains=buscar)
    return render(request, 'productos/listar_ventas.html', {'ventas': ventas})

@login_required
def crear_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentaForm()
    return render(request, 'productos/crear_venta.html', {'form': form})

@login_required
def modificar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentaForm(instance=venta)
    return render(request, 'productos/modificar_venta.html', {'form': form})

@login_required
def eliminar_venta(request, id):
    venta = get_object_or_404(Venta, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')
    return render(request, 'productos/eliminar_venta.html', {'venta': venta})

from rest_framework import viewsets
from .models import Marca, Producto, Venta
from .serializers import (
    MarcaSerializer, 
    ProductoAdminSerializer, 
    ProductoPublicoSerializer, 
    VentaSerializer
)

# 1. Vista para el Mantenedor 1 (Marca)
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

# 2. Vista para el Mantenedor 2 (Producto) con validación de perfiles
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    
    def get_serializer_class(self):
        # Si el usuario es administrador, usa el serializador que muestra todo
        if self.request.user and self.request.user.is_staff:
            return ProductoAdminSerializer
        # Si es usuario normal, usa el serializador que oculta precio y stock
        return ProductoPublicoSerializer

# 3. Vista para la Transacción (Venta)
class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
=======
from django.shortcuts import render, redirect
from .models import Producto, Venta
from .forms import VentaForm

# Vista principal del catálogo de productos
def lista_productos(request):
    buscar = request.GET.get('buscar', '')
    if buscar:
        productos = Producto.objects.filter(nombre__icontains=buscar)
    else:
        productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

# Vista de información
def info_productos(request):
    return render(request, 'productos/info.html')

# Vista para registrar y listar ventas
def registrar_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            producto = venta.producto
            if producto.stock >= venta.cantidad:
                producto.stock -= venta.cantidad
                producto.save()
                venta.save()
                return redirect('/productos/ventas/')
            else:
                form.add_error('cantidad', f'Stock insuficiente. Solo quedan {producto.stock} unidades.')
    else:
        form = VentaForm()

    ventas = Venta.objects.all().order_by('-fecha')
    return render(request, 'productos/ventas.html', {'form': form, 'ventas': ventas})
>>>>>>> 2228d9bb49f02df33e73c48eccaeac1cdc4c62bd
