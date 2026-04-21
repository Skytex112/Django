from django.urls import path
from . import views

urlpatterns = [
    path('weekday/', views.weekday_view),
    path('quote/', views.random_quote),
]