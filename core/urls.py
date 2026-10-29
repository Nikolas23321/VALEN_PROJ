from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('casas/', views.casas, name='casas'),
    path('sobre/', views.sobre, name='sobre'),
]