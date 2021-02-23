from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', views.add, name="add"),
    path('', views.update, name="update"),
    path('', views.delete, name="delete"),
    
]
