from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.forms import TaskForm, SubTaskForm, NoteForm, CategoryForm, PriorityForm
from task_manager.models import Task, SubTask, Note, Category, Priority

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
    ordering = ["id"] 

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
                )
        return qs

    def get_ordering(self):
        allowed = ["id", "title", "deadline"]
        sort_by = self.request.GET.get("sort_by", "id")
        sort_order = self.request.GET.get("sort_order", "desc")  # Get the order from request
        
        if sort_by not in allowed:
            sort_by = "id" # Default sort field
        
        # Add '-' prefix for descending order
        if sort_order == "desc":
            sort_by = f"-{sort_by}"
        
        return sort_by


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
    ordering = ["id"] 

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(parent_task__title__icontains=query)
                )
        return qs

    def get_ordering(self):
        allowed = ["id", "title", "parent_task__title"]
        sort_by = self.request.GET.get("sort_by", "id")
        sort_order = self.request.GET.get("sort_order", "desc")  # Get the order from request
        
        if sort_by not in allowed:
            sort_by = "id" # Default sort field
        
        # Add '-' prefix for descending order
        if sort_order == "desc":
            sort_by = f"-{sort_by}"
        
        return sort_by


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
    ordering = ["id"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(task__title__icontains=query) |
                Q(content__icontains=query)
                )
        return qs
    
    def get_ordering(self):
        allowed = ["id", "task__title"]
        sort_by = self.request.GET.get("sort_by", "id")
        sort_order = self.request.GET.get("sort_order", "desc")  # Get the order from request
        
        if sort_by not in allowed:
            sort_by = "id" # Default sort field
        
        # Add '-' prefix for descending order
        if sort_order == "desc":
            sort_by = f"-{sort_by}"
        
        return sort_by


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


# Category class views
class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = "category_list.html"
    paginate_by = 5
    ordering = ["id"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(name__icontains=query)
        return qs

    def get_ordering(self):
        allowed = ["id", "name"]
        sort_by = self.request.GET.get("sort_by", "id")
        sort_order = self.request.GET.get("sort_order", "desc")  # Get the order from request
        
        if sort_by not in allowed:
            sort_by = "id" # Default sort field
        
        # Add '-' prefix for descending order
        if sort_order == "desc":
            sort_by = f"-{sort_by}"
        
        return sort_by

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_del.html"
    success_url = reverse_lazy('category-list')


# Priority class views
class PriorityListView(ListView):
    model = Priority
    context_object_name = 'priorities'
    template_name = "priority_list.html"
    paginate_by = 5
    ordering =["id"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(name__icontains=query)
        return qs
    
    def get_ordering(self):
        allowed = ["id", "name"]
        sort_by = self.request.GET.get("sort_by", "id")
        sort_order = self.request.GET.get("sort_order", "desc")  # Get the order from request
        
        if sort_by not in allowed:
            sort_by = "id" # Default sort field
        
        # Add '-' prefix for descending order
        if sort_order == "desc":
            sort_by = f"-{sort_by}"
        
        return sort_by


class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy('priority-list')


class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy('priority-list')


class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = "priority_del.html"
    success_url = reverse_lazy('priority-list')