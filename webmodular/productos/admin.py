from django.contrib import admin
<<<<<<< HEAD
from .models import Marca, Producto

admin.site.register(Marca)
admin.site.register(Producto)
=======
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
    list_display = ('id', 'producto', 'cantidad', 'fecha')
    list_filter = ('fecha',)
>>>>>>> 2228d9bb49f02df33e73c48eccaeac1cdc4c62bd
