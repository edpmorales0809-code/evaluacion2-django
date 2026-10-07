from django import forms
<<<<<<< HEAD
from .models import Marca, Producto, Venta

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__' # Esto incluye todos los campos (nombre y descripción)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
=======
from .models import Venta
>>>>>>> 2228d9bb49f02df33e73c48eccaeac1cdc4c62bd

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
<<<<<<< HEAD
        fields = ['producto', 'cantidad']
=======
        fields = ['producto', 'cantidad']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-select'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }
>>>>>>> 2228d9bb49f02df33e73c48eccaeac1cdc4c62bd
