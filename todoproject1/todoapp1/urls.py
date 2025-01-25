from django.contrib import admin
from django.urls import path
from  . import  views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvindex/',views.TasklistView.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvUpdate/<int:pk>/',views.TaskUpdateView.as_view(),name='cbvUpdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='cbvdelete')
]







