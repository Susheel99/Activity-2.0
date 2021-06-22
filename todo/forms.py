from django import forms
from .models import SubTask,Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','task_desc','end_date']

    def __init__(self,*args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task_name'].widget.attrs['class'] = 'form-control'


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['sub_name', 'start_date','start_time','end_time']