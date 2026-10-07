from rest_framework import serializers
from .models import Marca, Producto, Venta

# 1. Serializador para Mantenedor 1
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

# 2. Serializadores para Mantenedor 2 (Cumpliendo el requerimiento de Perfiles)

# -> Perfil Administrador: Ve toda la información (incluye precio y stock)
class ProductoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

# -> Perfil Usuario: Oculta datos financieros/internos (precio y stock)
class ProductoPublicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'marca'] 

# 3. Serializador para la Transacción
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'