from django import forms
from .models import SubTask,Task

class DateInput(forms.DateInput):
    input_type = 'date'
class TaskForm(forms.ModelForm):
    class Meta:
        widgets = {'end_date': DateInput()}
        model = Task
        fields = ['task_name','task_desc','end_date']

    def __init__(self,*args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_desc'].widget.attrs['class'] = 'form-control'
        self.fields['end_date'].widget.attrs['class'] = 'form-control'
        


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['sub_name', 'start_date','start_time','end_time']

    def __init__(self,*args, **kwargs):
        super(SubTaskForm, self).__init__(*args, **kwargs)

        self.fields['sub_name'].widget.attrs['class'] = 'form-control'
        self.fields['start_date'].widget.attrs['class'] = 'form-control'
        self.fields['start_time'].widget.attrs['class'] = 'form-control'
        self.fields['end_time'].widget.attrs['class'] = 'form-control'