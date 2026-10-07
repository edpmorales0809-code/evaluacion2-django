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