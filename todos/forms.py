# todos/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description']  # IMPORTANTE: inclua description aqui
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título'}),
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Digite a descrição da tarefa'
            }),
        }
