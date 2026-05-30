from django.urls import path
from . import views

urlpatterns = [
    path('restaurants/', views.restaurants),
    path('delete/<int:id>/', views.delete_restaurant),
    path('edit/<int:id>/', views.edit_restaurant),
]