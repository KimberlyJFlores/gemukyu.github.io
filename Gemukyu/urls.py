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
from Gemukyu_App.views import game_list, home, shoppingCart
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path("admin/", admin.site.urls),
    path('games/', game_list, name='game_list'),
    path('shoppingCart/', shoppingCart, name='shoppingCart')
    path('game_page/', views.game_page, name='game_page'),
    path('game_page/add_to_cart/', views.add_to_cart, name='add_to_cart'),

    ]
urlpatterns += staticfiles_urlpatterns()
