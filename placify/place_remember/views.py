import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from social_django.models import UserSocialAuth

from .forms import MemoryForm
from .models import Memory


def get_vk_profile(request) -> dict:
    if not request.user.is_authenticated:
        return None
    vk_user = UserSocialAuth.objects.get(user=request.user)
    id = vk_user.uid
    access_token = vk_user.extra_data['access_token']
    url = (
        'https://api.vk.com/method/users.get?'
        f'user_ids={id}'
        '&fields=photo_100'
        f'&access_token={access_token}'
        '&v=5.131'
    )
    req = requests.get(
        url
    )

    res = req.json()
    vk_data = res['response'][0]
    return vk_data


def index(request):
    return render(request, 'place_remember/index.html',
                  {'data': get_vk_profile(request)})


@login_required(login_url='/')
def profile(request):
    vk_data = get_vk_profile(request)
    memories = Memory.objects.filter(user=request.user)
    return render(request, 'place_remember/profile.html',
                  {'data': vk_data,
                   'memories': memories})


def add_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = Memory(user=request.user,
                            title=request.POST.get('title'),
                            comment=request.POST.get('comment'),
                            latitude=request.POST.get('latitude'),
                            longitude=request.POST.get('longitude'))
            memory.save()
            return redirect('/profile')
    else:
        form = MemoryForm()

    return render(request, 'place_remember/add_memory.html',
                  {'form': form,
                   'data': get_vk_profile(request)})
