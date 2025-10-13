from django.shortcuts import render
from django.views.generic.list import ListView
from task_manager.models import Task

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = "home.html"