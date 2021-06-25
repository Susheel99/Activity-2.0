from django.shortcuts import render,redirect
from .models import Task,SubTask
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import SubTaskForm,TaskForm
import datetime
from itertools import chain

# Create your views here.

def index(request):
    tasks = Task.objects.filter(user=request.user).order_by('-end_date')
    return render(request,'todo/index.html',{'tasks':tasks})

def task_detail(request,id):
    form = SubTaskForm(request.POST or None)
    tasks = Task.objects.filter(user=request.user)
    task = Task.objects.get(id=id)
    sub_tasks = SubTask.objects.filter(task=task)
    return render(request,'todo/generic.html',{'task':task,'sub_tasks':sub_tasks,'form':form,'tasks':tasks})

def hide(request,id):
    subtask = SubTask.objects.get(id=id)
    subtask.is_active = False
    subtask.save()
    
    return HttpResponseRedirect(reverse('task_detail', args=(subtask.task.id,)))

def delete_subtask(self,id):
    subtask = SubTask.objects.get(id=id)
    subtask.delete()

    return HttpResponseRedirect(reverse('task_detail', args=(subtask.task.id,)))
    

def add(request,id):
    task = Task.objects.get(id=id)
    form = SubTaskForm(request.POST or None)

    if form.is_valid():
        subtask_name = form.cleaned_data['sub_name']
        start_time = form.cleaned_data['start_time']
        start_date = form.cleaned_data['start_date']
        end_time = form.cleaned_data['end_time']
        
        subtask = SubTask.objects.create(user=request.user,sub_name=subtask_name,start_date=start_date, start_time=start_time, end_time=end_time,task=task,is_active=True)
        subtask.save()
    
    return HttpResponseRedirect(reverse('task_detail', args=(task.id,)))
    
    
def add_task(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        task_name = form.cleaned_data['task_name']
        task_desc = form.cleaned_data['task_desc']
        # start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        task = Task.objects.create(user=request.user,task_name=task_name,task_desc=task_desc,end_date=end_date)
        task.save()
       
        return redirect('index')
    return render(request,'todo/add_task.html',{'form':form})

def delete_task(request,id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('index')

def all_tasks(request):
    today=datetime.date.today()  # Returns 2018-01-15
    # print(c)
    subtasks = SubTask.objects.filter(user=request.user,start_date=today).order_by('start_time')
    
    
    return render(request,'todo/all_tasks.html',{'subtasks':subtasks})

    
def pending_tasks(request):
    today=datetime.date.today()
    subtasks = SubTask.objects.filter(user=request.user,start_date__lt=today,is_active=True).order_by('start_time')
    return render(request,'todo/pending_tasks.html',{'subtasks':subtasks})

def subtasks_by_date(request):
    
    subtasks = None
    if request.method == 'POST':
        date = request.POST.get('date')
        subtasks = SubTask.objects.filter(user=request.user,start_date=date).order_by('start_time')
        
        return render(request,'todo/get_subtasksbydate.html',{'subtasks':subtasks,'day':date})
    return render(request,'todo/get_subtasksbydate.html',{'subtasks':subtasks})

def subtasks_by_task(request):
    tasks = Task.objects.filter(user=request.user)
    subtasks = None
    if request.method == 'POST':
        print('Yes')
        id = request.POST.get('id')
        print(id)
        task = Task.objects.get(id=id)
        subtasks = SubTask.objects.filter(user=request.user,task=task).order_by('start_time')
     
        return render(request,'todo/subtasks_by_task.html',{'subtasks':subtasks,'tasks':tasks})
    return render(request,'todo/subtasks_by_task.html',{'subtasks':subtasks,'tasks':tasks})