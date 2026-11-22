
from django.test import TestCase
from django.urls import reverse
from .models import Tarea


class TareaTests(TestCase):

    def setUp(self):
        self.tarea = Tarea.objects.create(
            titulo='Tarea inicial',
            descripcion='Descripción de prueba'
        )

    def test_listar_tareas(self):
        respuesta = self.client.get(reverse('listar_tareas'))

        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Tarea inicial')

    def test_registrar_tarea(self):
        respuesta = self.client.post(
            reverse('registrar_tarea'),
            {
                'titulo': 'Nueva tarea',
                'descripcion': 'Descripción nueva'
            }
        )

        self.assertRedirects(respuesta, reverse('listar_tareas'))
        self.assertTrue(
            Tarea.objects.filter(titulo='Nueva tarea').exists()
        )

    def test_editar_tarea(self):
        respuesta = self.client.post(
            reverse('editar_tarea', args=[self.tarea.id]),
            {
                'titulo': 'Tarea modificada',
                'descripcion': 'Descripción modificada'
            }
        )

        self.assertRedirects(respuesta, reverse('listar_tareas'))

        self.tarea.refresh_from_db()

        self.assertEqual(self.tarea.titulo, 'Tarea modificada')
        self.assertEqual(
            self.tarea.descripcion,
            'Descripción modificada'
        )

    def test_cambiar_estado(self):
        respuesta = self.client.post(
            reverse('cambiar_estado', args=[self.tarea.id])
        )

        self.assertRedirects(respuesta, reverse('listar_tareas'))

        self.tarea.refresh_from_db()

        self.assertTrue(self.tarea.completada)

    def test_eliminar_tarea(self):
        respuesta = self.client.post(
            reverse('eliminar_tarea', args=[self.tarea.id])
        )

        self.assertRedirects(respuesta, reverse('listar_tareas'))
        self.assertFalse(
            Tarea.objects.filter(id=self.tarea.id).exists()
        )
