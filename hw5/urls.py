from django.urls import path
from . import views

urlpatterns = [
    path('task1/', views.task1),
    path('task2/', views.task2),
    path('task3/', views.task3),
    path('task4/', views.task4),
]