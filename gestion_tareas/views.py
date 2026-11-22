
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Tarea
from .forms import TareaForm


def registrar_tarea(request):

    if request.method == 'POST':
        formulario = TareaForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_tareas')

    else:
        formulario = TareaForm()

    return render(request, 'gestion_tareas/registrar.html', {
        'formulario': formulario
    })


def listar_tareas(request):
    tareas = Tarea.objects.all().order_by('-fecha_creacion')

    return render(request, 'gestion_tareas/listar.html', {
        'tareas': tareas
    })


def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == 'POST':
        formulario = TareaForm(request.POST, instance=tarea)

        if formulario.is_valid():
            formulario.save()
            return redirect('listar_tareas')

    else:
        formulario = TareaForm(instance=tarea)

    return render(request, 'gestion_tareas/editar.html', {
        'formulario': formulario,
        'tarea': tarea
    })


@require_POST
def cambiar_estado(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.completada = not tarea.completada
    tarea.save()

    return redirect('listar_tareas')


@require_POST
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()

    return redirect('listar_tareas')
