from django import forms
from .models import SubTask

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['sub_name', 'start_time','end_time']