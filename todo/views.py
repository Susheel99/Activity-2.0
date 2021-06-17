from django.shortcuts import render,redirect
from .models import Task,SubTask
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SubTaskForm,TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    cnt = tasks.count()
    return render(request,'todo/index.html',{'tasks':tasks,'cnt':cnt})

def task_detail(request,id):
    form = SubTaskForm(request.POST or None)
    task = Task.objects.get(id=id)
    sub_tasks = SubTask.objects.filter(task=task)
    return render(request,'todo/generic.html',{'task':task,'sub_tasks':sub_tasks,'form':form})

def hide(request,id):
    subtask = SubTask.objects.get(id=id)
    subtask.is_active = False
    subtask.save()
    
    return HttpResponseRedirect(reverse('task_detail', args=(subtask.task.id,)))

def add(request,id):
    task = Task.objects.get(id=id)
    form = SubTaskForm(request.POST or None)

    if form.is_valid():
        subtask_name = form.cleaned_data['sub_name']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        
        subtask = SubTask.objects.create(sub_name=subtask_name, start_time=start_time, end_time=end_time,task=task,is_active=True)
        subtask.save()
    
    return HttpResponseRedirect(reverse('task_detail', args=(task.id,)))
    
    
def add_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
        # task_name = form.cleaned_data['task_name']
        # task_desc = form.cleaned_data['task_desc']
        # start_date = form.cleaned_data['start_date']
        # end_date = form.cleaned_data['end_date']
    return render(request,'todo/add_task.html',{'form':form})

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('index')

    
