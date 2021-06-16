from django.shortcuts import render
from .models import Task,SubTask
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    cnt = tasks.count()
    return render(request,'todo/index.html',{'tasks':tasks,'cnt':cnt})

def task_detail(request,id):
    task = Task.objects.get(id=id)
    sub_tasks = SubTask.objects.filter(task=task)
    return render(request,'todo/generic.html',{'task':task,'sub_tasks':sub_tasks})

def hide(request,id):
    subtask = SubTask.objects.get(id=id)
    # task = SubTask.objects.get(Task,)
   
    subtask.is_active = False
    subtask.save()
    

    return HttpResponseRedirect(reverse('task_detail', args=(subtask.task.id,)))
    
