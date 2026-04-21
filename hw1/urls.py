from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_datetime),
    path('table/', views.multiplication_table),
    path('programmer-day/', views.programmer_day),
]