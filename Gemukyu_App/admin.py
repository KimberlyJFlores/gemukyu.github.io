from django.contrib import admin
from .models import Cart, Developers, Games, OrderItems, Orders, Publishers, Reviews, Wishlist, Users

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('cart_id', 'user_id', 'game_id', 'quantity')

@admin.register(Developers)
class DevelopersAdmin(admin.ModelAdmin):
    list_display = ('developer_id', 'name', 'website')

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ('game_id', 'title', 'description', 'release_date', 'genre', 'price', 'publisher', 'pub_website', 'developer', 'dev_website', 'discount')

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order_item_id', 'order_id', 'game_id', 'quantity', 'item_price')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user_id', 'order_date', 'total_amount')

@admin.register(Publishers)
class PublishersAdmin(admin.ModelAdmin):
    list_display = ('publisher_id', 'name', 'website')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'user_id', 'game_id', 'rating', 'comment', 'review_date')

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'password', 'first_name', 'last_name', 'date_registered', 'last_login')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('wishlist_id', 'user_id', 'game_id', 'added_date')

"""@admin.register(Trending)
class TrendingAdmin(admin.ModelAdmin):
    list_display = ('game_id')

@admin.register(Foryou)
class ForyouAdmin(admin.ModelAdmin):
    list_display = ('game_id')"""

