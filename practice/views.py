from django.http import HttpResponse
from django.shortcuts import render
from prac.models import Task

def home(request):
    tasks=Task.objects.filter(is_completed=False)
    completed_task=Task.objects.filter(is_completed=True)
    context={'completed_task':completed_task, 'tasks':tasks}
    return render(request, 'home.html', context)