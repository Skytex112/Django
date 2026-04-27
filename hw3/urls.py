from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history_home),
    path('history/<int:year>/', views.history_year),
    

    path('cities/', views.cities_home),
    path('cities/<str:city>/<int:year>/', views.city_year),
]