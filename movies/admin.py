from django.contrib import admin
from .models import Movie,UserMovie,UserTvshow
# Register your models here.

admin.site.register(Movie) 
admin.site.register(UserMovie) 
admin.site.register(UserTvshow) 