from django.urls import path
from . import views

urlpatterns = [
    path('page/<str:page_number>/', views.show_page),
]