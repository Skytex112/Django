from django.urls import path
from .views import reviews_view

urlpatterns = [
    path('reviews/', reviews_view, name='reviews'),
]