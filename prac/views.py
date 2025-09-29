from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Task

def addtask(request):
    task1=request.POST['task']
    Task.objects.create(task=task1)
    return redirect('home')
def mark_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')
def mark_undone(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')
def edit_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new=request.POST['task']
        task.task=new
        task.save()
        return redirect('home')
    else:
        context={'task':task}
    return render(request,'edit_task.html',context)
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')



    