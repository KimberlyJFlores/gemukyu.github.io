from django.db import models

class Games(models.Model):
    game_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publisher = models.CharField(max_length=255,default="placeholder")
    pub_website = models.CharField(max_length=500,default="placeholder")
    developer = models.CharField(max_length=255, default="placeholder")
    dev_website = models.CharField(max_length=500, default="placeholder")
    discount = models.DecimalField(decimal_places=3, max_digits=5, default=0)
    small_pic = models.URLField(max_length=200, default="Gemukyu_App/static/images/GimukyuHomeIcon.png")
    big_pic = models.URLField(max_length=200, default="Gemukyu_App/static/images/GimukyuHomeIcon.png")

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Developers(models.Model):
    developer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

class OrderItems(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    game_id = models.IntegerField()
    quantity = models.IntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    order_date = models.DateTimeField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Publishers(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255)

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField()

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_registered = models.DateTimeField()
    last_login = models.DateTimeField()

class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    game_id = models.IntegerField()
    added_date = models.DateTimeField()

class Trending(models.Model):
    trending_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE)

class Foryou(models.Model):
    foryou_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE)