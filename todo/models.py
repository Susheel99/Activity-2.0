from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_desc = models.TextField(max_length=500)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    
    def __str__(self):
        return self.task_name

class SubTask(models.Model):
    sub_name = models.CharField(max_length=500)
    start_time = models.TimeField()
    end_time = models.TimeField()
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.sub_name