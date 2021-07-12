from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    image_url = models.URLField(max_length=500)
    title = models.CharField(max_length=500)
    imdb_id = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    cast = models.CharField(max_length=500)
    rank = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return self.title

class UserMovie(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchlist = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

class UserTvshow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watchlist = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    current_season = models.IntegerField()

