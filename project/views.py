from django.shortcuts import render
from .models import Project,Idea
from django.shortcuts import get_object_or_404
from .forms import  ProjectForm
# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request,'project/index.html',{'projects':projects})

def project_detail(request,id):
    project_dt = get_object_or_404(Project,id=id)
    ideas = Idea.objects.filter(project=project_dt)
    print(type(ideas))
    return render(request,'project/project_detail.html',{'ideas':ideas})

def add_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        # project_name = form.cleaned_data['project_name']
        # end_date = form.cleaned_data['end_date']
        # image = form.cleaned_data['image']
        # concept = form.cleaned_data['concept']

    return render(request,'project/add_project.html',{'form':form})