from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="start_page"),
    path('text/', views.text_format, name="text-format"),
    path('style/', views.style, name="style_page"),
    path('contacts/', views.constacts, name="contacts_page"),
    
]