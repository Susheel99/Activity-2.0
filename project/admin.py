from django.contrib import admin
from .models import *
#Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','start_date','end_date')

admin.site.register(Project,ProjectAdmin)
admin.site.register(Idea)