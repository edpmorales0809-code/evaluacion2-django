from django.db import models

class Marca(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Marca")
=======
    nombre = models.CharField(max_length=100)
>>>>>>> 2228d9bb49f02df33e73c48eccaeac1cdc4c62bd
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
<<<<<<< HEAD
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")
    stock = models.IntegerField(verbose_name="Stock disponible")
    
    # Esta línea genera la relación para tu transacción
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos', verbose_name="Marca del Producto")

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Venta(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, verbose_name="Producto Vendido")
    cantidad = models.IntegerField(verbose_name="Cantidad")
    fecha_venta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de la Venta")

    def __str__(self):
        return f"Venta: {self.cantidad} x {self.producto} - {self.fecha_venta.strftime('%d/%m/%Y')}"
=======
    nombre = models.CharField(max_length=150)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')
    precio = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.marca.nombre})"

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.cantidad} x {self.producto.nombre}"
>>>>>>> 2228d9bb49f02df33e73c48eccaeac1cdc4c62bd
