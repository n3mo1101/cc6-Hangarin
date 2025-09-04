from django.contrib import admin
from .models import Priority, Category, Task, SubTask, Note

# Register your models here.
admin.site.register(Priority)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Note)