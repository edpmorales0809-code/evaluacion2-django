from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Marca, Producto, Venta

class ProductoAPITestCase(TestCase):
    def setUp(self):
        # Crear datos de prueba
        self.marca = Marca.objects.create(nombre="Apple")
        self.producto = Producto.objects.create(
            nombre="iPhone 16",
            descripcion="Último modelo",
            precio=999.99,
            stock=10,
            marca=self.marca
        )
        
        # Cliente para pruebas de API
        self.client = APIClient()
        
        # Usuario administrador para probar el serializador admin
        self.admin_user = User.objects.create_superuser(
            username='admin', 
            password='adminpassword', 
            email='admin@test.com'
        )

    def test_listar_productos_publico(self):
        """Verifica que un usuario anónimo pueda ver los productos (perfil público)"""
        response = self.client.get('/productos/api/productos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Comprobar que no se exponen los campos sensibles en el perfil público
        data = response.json()
        self.assertNotIn('precio', data[0])
        self.assertNotIn('stock', data[0])

    def test_listar_productos_admin(self):
        """Verifica que un administrador vea todos los campos (precio y stock)"""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/productos/api/productos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn('precio', data[0])
        self.assertIn('stock', data[0])

    def test_crear_marca(self):
        """Verifica la creación de una marca mediante la API estando autenticado"""
        self.client.force_authenticate(user=self.admin_user)
        data = {"nombre": "Samsung"}
        response = self.client.post('/productos/api/marcas/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Marca.objects.count(), 2)
