from django import forms
from .models import SubTask,Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name','task_desc','end_date']


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['sub_name', 'start_time','end_time']