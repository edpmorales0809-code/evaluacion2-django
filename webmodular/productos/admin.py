from django.contrib import admin
from .models import Marca, Producto, Venta

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock', 'marca')
    search_fields = ('nombre',)
    list_filter = ('marca',)

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'cantidad', 'fecha')
    list_filter = ('fecha',)