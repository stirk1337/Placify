from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # render
    path('profile', views.profile),  # render
]
