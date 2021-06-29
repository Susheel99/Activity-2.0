from django.shortcuts import render,redirect
from .models import Project,Idea
from django.shortcuts import get_object_or_404
from .forms import  ProjectForm,IdeaForm
from django.urls import reverse
from django.http import HttpResponseRedirect
import PIL
from PIL import Image
# Create your views here.

def home(request):
    projects = Project.objects.filter(user=request.user)
    return render(request,'project/index.html',{'projects':projects})

def project_detail(request,id):
    form = IdeaForm(request.POST or None)
    project_dt = get_object_or_404(Project,id=id)
    ideas = Idea.objects.filter(project=project_dt)

    if form.is_valid():
        idea_desc = form.cleaned_data['idea_desc']
        project_dt = get_object_or_404(Project,id=id)
        idea_form = Idea.objects.create(idea_desc=idea_desc,project = project_dt)
        idea_form.save()
        return HttpResponseRedirect(reverse('project_detail', args=(id,)))
        # form.clear()
        #return render(request,'project/project_detail.html',{'ideas':ideas,'form':form,'project':project_dt})
        # return redirect('project_detail',args=(id,))



    return render(request,'project/project_detail.html',{'ideas':ideas,'form':form,'project':project_dt})

def add_project(request):
    form = ProjectForm(request.POST or None,request.FILES or None)


    if form.is_valid():
        project_name = form.cleaned_data['project_name']
        end_date = form.cleaned_data['end_date']
        image = form.cleaned_data['image']
        concept = form.cleaned_data['concept']
        project = Project.objects.create(user=request.user,project_name=project_name,image=image,concept=concept,end_date=end_date)
        project.save()
        return redirect('home')

    return render(request,'project/add_project.html',{'form':form})

def project_delete(request,id):
    project=Project.objects.filter(id=id)
    project.delete()

    return redirect('home')

def webmainpage(request):
    return render(request,'project/homepage.html')