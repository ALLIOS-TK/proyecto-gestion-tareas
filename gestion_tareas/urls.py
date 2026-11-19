from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tareas, name='listar_tareas'),
    path('registrar/', views.registrar_tarea, name='registrar_tarea'),
]
