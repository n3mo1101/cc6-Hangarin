from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.forms import TaskForm, SubTaskForm, NoteForm
from task_manager.models import Task, SubTask, Note

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"


# Task class views
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "task_list.html"
    paginate_by = 5


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task_del.html"
    success_url = reverse_lazy('task-list')


# Subtask class views
class SubTaskListView(ListView):
    model = SubTask
    context_object_name = 'subtasks'
    template_name = "subtask_list.html"
    paginate_by = 5


class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy('subtask-list')


class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy('subtask-list')


class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = "subtask_del.html"
    success_url = reverse_lazy('subtask-list')


# Note class views
class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = "note_list.html"
    paginate_by = 5


class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy('note-list')


class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy('note-list')


class NoteDeleteView(DeleteView):
    model = Note
    template_name = "note_del.html"
    success_url = reverse_lazy('note-list')