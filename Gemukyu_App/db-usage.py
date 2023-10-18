from models import *

def addGameToCart(userId, gameId):
    gameCheck = Cart.objects.filter(userId=userId, gameId=gameId)
    if (gameCheck == None):
        gameToAdd = Cart(userId=userId, gameId=gameId, quantity=1) #missing cart id
        gameToAdd.save()
    else:
        print("Error: Game already in cart") 
    
def removeGameFromCart(gameId, userId):
    game = Cart.objects.get(gameId=gameId, userId=userId) # i think this 
    game.delete()
