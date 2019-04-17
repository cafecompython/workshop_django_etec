from django import forms
from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['coment_autor', 'coment_texto']
        labels = {
            'coment_autor': '',
            'coment_texto': '',

        }
        widgets = {
            'coment_autor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'placeholder': 'Digite seu nome',
                    }
                ),
             'coment_texto': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3', 
                }
            ),
        }
