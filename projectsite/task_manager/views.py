from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.forms import TaskForm
from task_manager.models import Task

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"


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