from rest_framework import serializers
from .models import Marca, Producto, Venta

class MarcaSerializer(serializers.ModelSerializer):
    class Metadata:
        model = Marca
        fields = '__all__'

    class Meta:
        model = Marca
        fields = ['id', 'nombre']

# Serializador para el perfil público (oculta precio y stock)
class ProductoPublicoSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.ReadOnlyField(source='marca.nombre')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'marca_nombre']

# Serializador para el perfil de Administrador (muestra todo e incluye validaciones)
class ProductoAdminSerializer(serializers.ModelSerializer):
    marca_nombre = serializers.ReadOnlyField(source='marca.nombre')

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'marca', 'marca_nombre']

    # Validación personalizada exigida en pautas avanzadas: el precio no puede ser negativo
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio del producto debe ser mayor a 0.")
        return value

    # Validación de stock
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock no puede ser un valor negativo.")
        return value

class VentaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.ReadOnlyField(source='producto.nombre')

    class Meta:
        model = Venta
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'fecha']

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("La cantidad de venta debe ser al menos 1.")
        return value