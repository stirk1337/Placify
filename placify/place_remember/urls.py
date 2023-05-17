from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # render
    path('profile', views.profile),  # render
    path('add_memory', views.add_memory)  # post
]
