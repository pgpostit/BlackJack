from functions import *      #Import all functions from functions.py
BlackJack = True             #Main condition to start the game in loop

#Output
display()

#Main game
while BlackJack:
    ans = input("Do you want to play BlackJack? 'y' or 'n' ").lower()         #Input to start the game. Accept only y and no.
    if ans == 'y':
        BlackJack = main_game()
    elif ans == 'n':
        print('Ok, bye!')
        break
    else:
        print('Please type a valid answer.')


