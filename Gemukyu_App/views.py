from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Games

def home(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Publisher: {game.release_date}")
    return render(request, 'template.html', {'games': games})

def game_list(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Publisher: {game.release_date}")
    return render(request, 'template.html', {'games': games})
