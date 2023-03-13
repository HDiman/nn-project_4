from .models import Task
from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название актива'
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите кол-во'
            }),
        }
