from django import forms
from .models import Project,Idea

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name','end_date','image','concept']

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['idea_desc']

    def __init__(self,*args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)

        self.fields['idea_desc'].widget.attrs['placeholder'] = "New Idea"