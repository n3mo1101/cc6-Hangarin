from django.forms import ModelForm
from django import forms
from .models import Task, SubTask, Note, Category, Priority


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            'deadline': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',   
                    'class': 'form-control', 
                }
            ),
        }


class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"