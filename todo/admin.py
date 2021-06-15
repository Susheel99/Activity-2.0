from django.contrib import admin
from .models import Task,SubTask


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name','start_date','end_date')

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('sub_name','start_time','end_time','task')

admin.site.register(Task,TaskAdmin)
admin.site.register(SubTask,SubTaskAdmin)