from django import forms
from .models import Tarea


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion']

        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe el título de la tarea'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe la descripción de la tarea',
                'rows': 4
            })
        }
