from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # render
    path('profile', views.profile, name='profile'),  # render
    path('add_memory', views.add_memory, name='add_memory'),  # post
    path('get_vk_profile', views.get_vk_profile, name='get_vk_profile')  # get
]
