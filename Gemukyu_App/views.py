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
        print(f"Title: {game.title}, Description: {game.description}, Release Date: {game.release_date}")
    return render(request, 'games_list.html', {'games': games})

def home(request):
    games = Games.objects.all()
    return render(request,'home.html', {'games': games})

def game_page(request):
    games = Games.objects.all()
    return render(request,'game_page.html', {'games': games})

#TODO Needs game_id and quantity. cart_id is autofield.

def add_to_cart(request):
    # This is just for demonstration; you'd fetch game_id and quantity based on your application's requirements.
    game_id = 2
    quantity = 1
    cart_id = request.session.get('cart_id')
    
    if not cart_id:
        new_cart = Cart.objects.create(user_id=None)  # No user since they're not logged in.
        request.session['cart_id'] = new_cart.id
        cart_id = new_cart.id

    cart_item, created = Cart.objects.get_or_create(cart_id=cart_id, game_id=game_id)
    
    if created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity
    cart_item.save()

    return HttpResponseRedirect(reverse('game_page'))

def order_confirmation(request):
    order_items = OrderItems.objects.filter(order_id=request.session.get('order_id', None))
    return render(request, 'order_confirmation.html', {'order_items': order_items})

def order_on_cart(request):
    cart_items = Cart.objects.filter(id=request.session.get('cart_id', None))
    total_price = sum([item.game.price * item.quantity for item in cart_items])
    sales_tax = 0.082 * total_price  # Just an example for 8.2% sales tax
    grand_total = total_price + sales_tax
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'sales_tax': sales_tax,
        'grand_total': grand_total,
    }

    return render(request, 'order_on_cart.html', context)
