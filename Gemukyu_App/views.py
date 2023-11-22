

# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
#from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .tables import GamesTable
from .filters import GamesFilter
import datetime
import time #for testing purposes

class GamesListView(SingleTableMixin, FilterView):
    table_class = GamesTable
    model = Games
    template_name = 'gamelist.html'
    filterset_class = GamesFilter

def game_list(request):
    games = Games.objects.all()
    for game in games:
        print(f"Title: {game.title}, Description: {game.description}, Release Date: {game.release_date}")
    return render(request, 'games_list.html', {'games': games})

def home(request):
    games = Games.objects.all()
    carts = Cart.objects.all()

    gameFilter = GamesFilter(request.GET, queryset=Games.objects.all())
    numCartItems = Cart.objects.filter(user_id=request.user.id).count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0
    context = {'games': games, 'cart': carts, 'numCartItems': numCartItems, 'gameFilter': gameFilter,
               }
    return render(request,'home.html', context)

def checkout(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    numCartItems = cart.count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0

    subtotal = sum(item.game_id.price for item in cart)
    sales_tax = '%.2f'%(float(0.0825) * float(subtotal))  # Just an example for 8.25% sales tax
    grand_total = '%.2f'%(float(subtotal) + float(sales_tax))

    try:
        discount = discount_codes.objects.get(discount_name=discount_codes).discount_value
    except discount_codes.DoesNotExist:
            discount = 0

    discounted_subtotal = subtotal - discount
    sales_tax = '%.2f'%(float(0.0825) * float(discounted_subtotal))
    grand_total = '%.2f'%(float(discounted_subtotal) + float(sales_tax))
  
    context = {
        'numCartItems': numCartItems,
        'subtotal': subtotal,
        'discount': discount,
        'sales_tax': sales_tax,
        'grand_total': grand_total
    }
    return render(request,'checkout.html', context)

def applyDiscount(request, discount_code):

    return redirect('checkout')

def purchaseCart(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    subtotal = sum(item.game_id.price for item in cart)
    sales_tax = '%.2f'%(float(0.0825) * float(subtotal))
    grand_total = '%.2f'%(float(subtotal) + float(sales_tax))

    #discounted_total = grand_total * cart.applied_discount

    newOrder = Orders.objects.create(user_id=request.user.id, 
                                     order_date=datetime.date.today(), total_amount=grand_total)
    newOrder.save()

    for cartItem in cart:
        newOrderItem = OrderItems.objects.create(order_id=newOrder.order_id,
                                          game_id=cartItem.game_id.game_id, quantity=1, 
                                          item_price=cartItem.game_id.price)
        newOrderItem.save()
        cartItem.delete()

    return redirect('order_confirmation', o_id=newOrder.order_id)

@login_required(login_url='login_user')
def shoppingCart(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    numCartItems = cart.count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0
    estimateTotal = 0

    for cartItem in cart:
        estimateTotal += cartItem.game_id.price

    sales_tax = float(0.0825) * float(estimateTotal)
    grand_total = float(estimateTotal) + float(sales_tax)

    context = { 
               'numCartItems': numCartItems,
               'cart': cart,
               'sales_tax': sales_tax,
               'estimateTotal': estimateTotal,
               'grand_total': grand_total}

    return render(request,'shoppingCart.html', context)

@login_required(login_url='login_user')
def remove_from_cart(request):
    cart_item_id = request.POST.get('cart_item_id')
    #print(cart_item_id)
    cart_item = get_object_or_404(Cart, cart_id=cart_item_id)

    if (cart_item.user_id == request.user.id):
        cart_item.delete()
        #messages.success(request, "Item removed from your cart.")
    
    return redirect('shoppingCart')

def game_page(request, g_id=192):
    games = Games.objects.all()
    numCartItems = Cart.objects.filter(user_id=request.user.id).count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        search = request.POST.get('searchInput')

        # coming from home page
        if (game_id is not None) and (game_id != ""):
            return render(request,'game_page.html', {'games': games, 'game_id': game_id, 'numCartItems': numCartItems})
        
        # coming from search bar
        if (search is not None) and (search != ""):
            try:
                foundGame = Games.objects.get(title=search)
                game_id = foundGame.game_id
                return render(request,'game_page.html', {'games': games, 'game_id': game_id, 'numCartItems': numCartItems}) # found this game
            except:
                print("ERROR: Couldn't find game with title '%s'." % search)
                return redirect('home') # didn't find this game
    else:
        games = Games.objects.all()
        numCartItems = Cart.objects.filter(user_id=request.user.id).count()

        if (g_id is not None) and (g_id != ""):
            return render(request,'game_page.html', {'games': games, 'game_id': g_id, 'numCartItems': numCartItems})
        return redirect('home')
            
def account_page(request):
    return render(request,'account.html');

#TODO Needs game_id and quantity. cart_id is autofield.

def add_to_cart(request):

    if not request.user.is_authenticated:
        return redirect('login_user')
    
    game_id = request.POST.get('game_id')
    if (game_id is not None) and (game_id != ""):
        cartItem = Cart(game_id=Games.objects.get(game_id=game_id), user_id=request.user.id, quantity=1)
        cartItem.save()
        return redirect('home')
    else:
        return redirect('home')

def order_confirmation(request, o_id):
    cart = Cart.objects.filter(user_id=request.user.id)
    numCartItems = cart.count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0
    estimateTotal = 0

    for cartItem in cart:
        estimateTotal += cartItem.game_id.price

    order_id = o_id

    order = Orders.objects.filter(order_id=order_id)
    order_items = OrderItems.objects.filter(order_id=order_id) # after billy finishes checkout
    games = []
    for game in order_items:
        games.append(Games.objects.get(game_id=game.game_id))

    subtotal = 0

    for item in order_items:
        subtotal += item.item_price * item.quantity 

    grand_total = '%.2f'%(float(subtotal) * float(1.0825))
    
    context = {
        'order_id' : order_id,
        'order': order,
        'games': games,
        'grand_total': grand_total,
        'numCartItems': numCartItems
    }
    
    return render(request, 'order_confirmation.html', context)

def order_on_cart(request):
    cart_items = Cart.objects.filter(id=request.session.get('cart_id', None))
    total_price = sum([item.game.price * item.quantity for item in cart_items])
    sales_tax = 0.0825 * total_price  # Just an example for 8.25% sales tax
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
    numCartItems = Cart.objects.filter(user_id=request.user.id).count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0
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
        return render(request, 'registration.html',{'numCartItems':numCartItems})
    
def login_user(request):
    numCartItems = Cart.objects.filter(user_id=request.user.id).count()
    if numCartItems is None or numCartItems == "":
        numCartItems = 0
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html', {'numCartItems': numCartItems})
    
def logout_user(request):
    logout(request)
    return redirect('home')