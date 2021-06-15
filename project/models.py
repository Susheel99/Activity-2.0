from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=50,)
    concept = models.TextField(max_length=500)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    image = models.ImageField(upload_to='photos/project',blank=True)

    def __str__(self):
        return self.project_name

class Idea(models.Model):
    idea_desc = models.CharField(max_length=500)
    added_date = models.DateField(auto_now=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.idea_desc[0:10]
