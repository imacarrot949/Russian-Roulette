from random import *
from art import *
tprint('Russian Roulette')
print('Made by ')
global Lrounds
Lrounds = 1
global Erounds
Erounds = 6 - Lrounds
def game():
    print('There are', Lrounds, 'live rounds.')
    print('There are', Erounds, 'blank rounds.')
    shoot = input('Would you like to shoot yourself or them, (Y/T)')
    if shoot == 'Y' or shoot == 'y':
        luck = randint(1, 6)
        if luck == Lrounds:
            print("You shot yourself, but it's not over, try again.")
            lose()
        if luck != Lrounds:
            print("You survived, pure luck.")
            survived()
    elif shoot == 'T' or shoot == 't':
        sluck = randint(1, 6)
        if sluck == Lrounds:
            print("You shoot them, not your doing.")
        elif sluck != Lrounds:
            print("You don't shoot.")
            survived()
            
def survived():
    print("It's their turn now, they shoot.")
    if randint(1, 6) == 1:
        print('You lose.')
        lose()
    else:
        print('You survive.')
    print('More bullets are now in the gun.')
    Lrounds = 2
    Erounds = 6 - Lrounds
    print('There are', Lrounds, 'live rounds.')
    print('There are', Erounds, 'blank rounds.')
    shoot = input('Would you like to shoot yourself or them, (Y/T)')
    if shoot == 'Y' or shoot == 'y':
        luck = randint(1, 6)
        if luck == Lrounds:
            print("You shot yourself, but it's not over, try again.")
            lose()
        if luck != Lrounds:
            print("You survived, pure luck.")
            survived1()
    elif shoot == 'T' or shoot == 't':
        sluck = randint(1, 6)
        if sluck == Lrounds:
            print("You shoot them, not your doing.")
        elif sluck != Lrounds:
            print("You don't shoot.")
            survived1()
    
def survived1():
    print("It's their turn now, they shoot.")
    if randint(2, 6) == 1:
        print('You lose.')
        lose()
    else:
        print('You survive.')
    print('More bullets are now in the gun.')
    Lrounds = 4
    Erounds = 6 - Lrounds
    print('There are', Lrounds, 'live rounds.')
    print('There are', Erounds, 'blank rounds.')
    shoot = input('Would you like to shoot yourself or them, (Y/T)')
    if shoot == 'Y' or shoot == 'y':
        luck = randint(1, 6)
        if luck == Lrounds:
            print("You shot yourself, but it's not over, try again.")
            lose()
        if luck != Lrounds:
            print("You survived, pure luck.")
            survived2()
    elif shoot == 'T' or shoot == 't':
        sluck = randint(1, 6)
        if sluck == Lrounds:
            print("You shoot them, not your doing.")
        elif sluck != Lrounds:
            print("You don't shoot.")
            survived2()

def survived2():
    print("It's their turn now, they shoot.")
    if randint(4, 6) == 1:
        print('You lose.')
        lose()
    else:
        print('You survive.')
    print('More bullets are now in the gun.')
    Lrounds = 5
    Erounds = 6 - Lrounds
    print('There are', Lrounds, 'live rounds.')
    print('There are', Erounds, 'blank rounds.')
    shoot = input('Would you like to shoot yourself or them, (Y/T)')
    if shoot == 'Y' or shoot == 'y':
        luck = randint(1, 6)
        if luck == Lrounds:
            print("You shot yourself, but it's not over, try again.")
            lose()
        if luck != Lrounds:
            print("You survived, pure luck. You win.")
            win()
    elif shoot == 'T' or shoot == 't':
        sluck = randint(1, 6)
        if sluck == Lrounds:
            print("You shoot them, not your doing.")
            win()
        elif sluck != Lrounds:
            print("You don't shoot.")
            print("They shoot you, you lose.")
            lose()
            
def win():
    input('You won, but was it worth it?')  
    
def lose():
    input('You lose, ask them if it was worth it.')     
    exit()
game()
