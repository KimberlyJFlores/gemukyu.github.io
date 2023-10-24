from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.template import loader
from .models import *

def game_list(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Publisher: {game.release_date}")
    return render(request, 'home.html', {'games': games})

def home(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Publisher: {game.release_date}")
    return render(request,'home.html', {'games': games})

def game_page(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Publisher: {game.release_date}")
    return render(request,'game_page.html', {'games': games})

#TODO Needs user_id and game_id, maybe cart_id but maybe do cart_id = user_id?

def add_to_cart(request):
    #game = Games.objects.get(game_id)
    #gameId = request.POST[1]
    cartItem = Cart(game_id=1, user_id=1, quantity=1, cart_id=1)
    cartItem.save()
    return HttpResponseRedirect(reverse('game_page'))
