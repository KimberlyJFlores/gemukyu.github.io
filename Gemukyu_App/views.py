

# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
#from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def game_list(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Release Date: {game.release_date}")
    return render(request, 'games_list.html', {'games': games})

def home(request):
    games = Games.objects.all()
    return render(request,'home.html', {'games': games})

def shoppingCart(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Publisher: {game.release_date}")
    return render(request,'shoppingCart.html', {'games': games})

def game_page(request):
    games = Games.objects.all()
    return render(request,'game_page.html', {'games': games})

def account_page(request):
    return render(request,'account.html');

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
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'sales_tax': sales_tax,
        'grand_total': grand_total,
    }

    return render(request, 'order_on_cart.html', context)



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.save()
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'registration.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #user = User.objects.create_user('Test', 'email@email.com', 'Test')
        #above code creates account, format: (username, email, password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')

def search(request):
    if request.method == 'POST':
        search = request.POST['searchInput']
        if Games.objects.filter(title__contains=search):
            game_id = str(getattr(Games, 'game_id'))
            return redirect('game_page') # redirect to game_page w/ game_id
        else:
            return redirect('home')