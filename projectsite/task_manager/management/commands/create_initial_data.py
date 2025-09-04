from django.core.management.base import BaseCommand
from faker import Faker
from django.utils import timezone
from task_manager.models import Priority, Category, Task, SubTask, Note

class Command(BaseCommand):
    help = 'Create initial data for the application'    
        
    def handle(self, *args, **kwargs):
        self.create_task(5)
        self.create_subtask(5)
        self.create_note(5)


    def create_task(self, count):
        fake = Faker()
        status_choices = [choice[0] for choice in Task._meta.get_field("status").choices]

        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=5).title(),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=status_choices),
                category=Category.objects.order_by('?').first(),
                priority=Priority.objects.order_by('?').first(),
            )

        self.stdout.write(self.style.SUCCESS(
        'Initial data for task created successfully.'))

    
    def create_subtask(self, count):
        fake = Faker()
        status_choices = [choice[0] for choice in SubTask._meta.get_field("status").choices]

        for _ in range(count):
            SubTask.objects.create(
                parent_task=Task.objects.order_by('?').first(),
                title=fake.sentence(nb_words=5).title(),
                status=fake.random_element(elements=status_choices),
            )

        self.stdout.write(self.style.SUCCESS(
        'Initial data for subtask created successfully.'))

    
    def create_note(self, count):
        fake = Faker()

        for _ in range(count):
            Note.objects.create(
                task=Task.objects.order_by('?').first(),
                content=fake.paragraph(nb_sentences=3),
            )
        
        self.stdout.write(self.style.SUCCESS(
        'Initial data for note created successfully.'))