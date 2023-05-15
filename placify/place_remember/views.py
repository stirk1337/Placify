from django.shortcuts import render


def index(request):
    return render(request, 'place_remember/index.html')
