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

#TODO Needs user_id and game_id, cart_id is autofield

def add_to_cart(request):
    cartItem = Cart(game_id=2, user_id=1, quantity=1)
    cartItem.save()
    return HttpResponseRedirect(reverse('game_page'))
