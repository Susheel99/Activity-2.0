from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from django.db.models import Count, TimeField
from django.db.models.functions import TruncHour
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=500)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

    def __str__(self):
        return self.task_name

    def get_subtasks(self):
        subtasks = SubTask.objects.filter(task=self,is_active=True)
        return len(subtasks)
    
    



class SubTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    sub_name = models.CharField(max_length=500)
    start_date = models.DateField(default=timezone.now, blank=True,null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_name

    # def timediff(self):
    #     experiments_per_hour = SubTask.objects.annotate(
    #     hour=TruncHour('start_time', output_field=TimeField()),).values('hour').annotate(experiments=Count('id'))
    #     for exp in experiments_per_hour:
    #         print(type(exp['hour']), exp['experiments'])
    #     return 0
