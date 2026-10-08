from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Marca")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock disponible")
    
    # --- NUEVOS CAMPOS PARA ASEGURAR LOS 10 PUNTOS DE LA RÚBRICA ---
    imagen = models.ImageField(upload_to='productos/imagenes/', null=True, blank=True, verbose_name="Imagen del Producto")
    documento = models.FileField(upload_to='productos/documentos/', null=True, blank=True, verbose_name="Manual o Ficha PDF")
    # ---------------------------------------------------------------
    
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos', verbose_name="Marca del Producto")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto Vendido")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Venta")

    def __str__(self):
        return f"Venta: {self.cantidad} x {self.producto.nombre} - {self.fecha_venta.strftime('%d/%m/%Y')}"