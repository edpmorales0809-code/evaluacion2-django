from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre de Categoría")
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Esta línea genera la relación obligatoria para la transacción
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias')

    def __str__(self):
        return self.titulo