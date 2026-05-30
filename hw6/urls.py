from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.user_login),

    path('books/', views.books),
    path('readers/', views.readers),

    path('add-book/', views.add_book),
    path('add-reader/', views.add_reader),

    path('take-book/<int:book_id>/', views.take_book),
]