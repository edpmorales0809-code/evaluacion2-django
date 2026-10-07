from django import forms
from .models import Marca, Producto, Venta

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__' # Esto incluye todos los campos (nombre y descripción)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['producto', 'cantidad']