from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    # Relación de clave foránea (Obligatoria para la rúbrica relacional)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta de {self.cantidad} unidad(es) de {self.producto.nombre}"