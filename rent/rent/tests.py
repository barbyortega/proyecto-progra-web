from django.test import TestCase
from django.urls import reverse
from .models import Genero, Cliente, Auto
from datetime import date

class ClienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        genero = Genero.objects.create(genero='Masculino')
        Cliente.objects.create(rut='12345678-9', nombre='Juan', apellido_paterno='Pérez', 
                               apellido_materno='González', fecha_nacimiento=date(1990, 5, 15),
                               genero=genero, telefono='987654321', email='juan@example.com',
                               direccion='Calle Falsa 123')

    def test_nombre_completo_cliente(self):
        cliente = Cliente.objects.get(rut='12345678-9')
        self.assertEqual(str(cliente), 'Juan Pérez')

    def test_email_cliente(self):
        cliente = Cliente.objects.get(rut='12345678-9')
        self.assertEqual(cliente.email, 'juan@example.com')

    # Aquí podrías agregar más pruebas para otros campos y validaciones de Cliente


class AutoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Auto.objects.create(marca='Toyota', nombre='Corolla', color='Rojo', 
                            cantidad_pasajeros=5, annio=2020, tipo_vehiculo='Sedan', 
                            combustible='Gasolina', valor=25000.00)

    def test_nombre_completo_auto(self):
        auto = Auto.objects.get(marca='Toyota')
        self.assertEqual(str(auto), 'Toyota Corolla')

    def test_tipo_vehiculo_auto(self):
        auto = Auto.objects.get(marca='Toyota')
        self.assertEqual(auto.tipo_vehiculo, 'Sedan')

    # Aquí podrías agregar más pruebas para otros campos y validaciones de Auto


class IndexViewTest(TestCase):

    def test_index_view_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')

    # Aquí podrías agregar más pruebas para verificar el contenido y funcionalidad de la vista Index

