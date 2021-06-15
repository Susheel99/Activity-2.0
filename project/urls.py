from django.contrib import admin
from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.project_detail, name='project_detail'),
    path('add_project/',views.add_project, name='add_project'),
    path('detail/<int:id>/project_delete/',views.project_delete, name='project_delete'),
]
