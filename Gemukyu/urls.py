"""
URL configuration for Gemukyu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gemukyu_App import views
from Gemukyu_App.views import game_list, home, shoppingCart, GamesListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path(r'admin/', admin.site.urls),
    path(r'games/', game_list, name='game_list'),
    path(r'shoppingCart/', shoppingCart, name='shoppingCart'),
    path(r'game_page/', views.game_page, name='game_page'),
    path('game_page/<int:g_id>/', views.game_page, name='game_pageId'),
    path(r'game_page/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path(r'register/', views.register, name='register'),
    path(r'login_user/', views.login_user, name='login_user'),
    path(r'logout_user/', views.logout_user, name='logout_user'),
    path(r'account/',views.account_page,name='account'),
    path(r'purchaseCart/order_confirmation/<int:o_id>', views.order_confirmation, name='order_confirmation'),
    path(r'order_on_cart/', views.order_on_cart, name='order_on_cart'),
    path(r'remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path(r'checkout/', views.checkout, name='checkout'),
    path('gamelist/', GamesListView.as_view(), name='gamelist'),
    path('purchaseCart/', views.purchaseCart, name='purchaseCart'),
    ]
urlpatterns += staticfiles_urlpatterns()
