from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('task_detail/<int:id>/',views.task_detail, name='task_detail'),
    path('hide/<int:id>/', views.hide, name='hide'),
    path('add/<int:id>/', views.add, name='add'),
    path('add_task/', views.add_task, name='add_task'),
]