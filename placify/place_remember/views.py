from django.shortcuts import render
import requests
from social_django.models import UserSocialAuth
from .models import Memory


def index(request):
    return render(request, 'place_remember/index.html')


def profile(request):
    vk_user = UserSocialAuth.objects.get(user=request.user)
    id = vk_user.uid
    access_token = vk_user.extra_data['access_token']
    req = requests.get(f'https://api.vk.com/method/users.get?user_ids={id}&fields=photo_100&access_token={access_token}&v=5.131')
    res = req.json()
    vk_data = res['response'][0]

    memories = Memory.objects.filter(user=request.user)
    return render(request, 'place_remember/profile.html',
                  {'data': vk_data,
                   'memories': memories})
