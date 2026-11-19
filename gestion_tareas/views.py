from django.shortcuts import render, redirect
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

