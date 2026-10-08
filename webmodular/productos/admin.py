from django.contrib import admin
from .models import Marca, Producto, Venta

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'marca', 'precio', 'stock')
    list_filter = ('marca',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad', 'fecha_venta')
    list_filter = ('fecha_venta',)