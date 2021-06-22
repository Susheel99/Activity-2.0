from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('task_detail/<int:id>/',views.task_detail, name='task_detail'),
    path('hide/<int:id>/', views.hide, name='hide'),
    path('add/<int:id>/', views.add, name='add'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('all_tasks/',views.all_tasks, name='all_tasks'),
    path('delete_subtask/<int:id>/', views.delete_subtask, name='delete_subtask')
]