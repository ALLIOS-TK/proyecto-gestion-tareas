
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tareas, name='listar_tareas'),
    path('registrar/', views.registrar_tarea, name='registrar_tarea'),
    path('editar/<int:id>/', views.editar_tarea, name='editar_tarea'),
    path('cambiar-estado/<int:id>/', views.cambiar_estado, name='cambiar_estado'),
    path('eliminar/<int:id>/', views.eliminar_tarea, name='eliminar_tarea'),
]
