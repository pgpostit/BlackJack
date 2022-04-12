#Imports
from art import logo
from random import choice
from variables import deck_list
from time import sleep


#Functions
##Game Display
def display():
    print(logo)

##Function to sort cards and remove the sorted card from the decklist
def sort_cards():
    deck_sorted = choice(deck_list)
    card_sorted = choice(deck_sorted)
    deck_sorted.remove(card_sorted)
    return card_sorted

##Function to count the value of cards
def count_cards(hand):
    total = 0
    for card in hand:
        total +=card
    return total

##Function to convert symbol cards into integers. Players can choose the value of Ace, but computer will randomly choose it.
def card_check(card, player='Dealer', pcount=50):
    if card == 'J' or card == 'Q' or card == 'K':
        card = 10
    elif card == 'A':
        if player == 'Player':
            while True:
                try:
                    choose = int(input('Do you want your A as 1 or 11? '))
                    if choose == 1 or choose == 11:
                        break
                except:
                    print('Please type 1 or 11.')
            if choose == 1:
                card = 1
            elif choose == 11:
                card = 11
        else:
            if pcount <=10:
                choose = 11
                card = choose
            else:
                choose = 1
                card = choose
    return card


##General hand rules. This function will give the cards to the players, use functions to convert the values and return the hand and the count to each player
def hand_rules(player='Dealer'):
    hand = [sort_cards(), sort_cards()]
    print('='*50)
    print(f'{player} cards: {hand}')
    for card in hand:
        if card == 'A':
            if player == 'Player':
                hand[hand.index(card)] = card_check(card, player)
            else:
                if ('Q', 'J', 'K', 10, 9, 8) in hand:
                    choose = 11
                    hand[hand.index[card]] = choose
                else:
                    choose = choice([1,11])
                    hand[hand.index(card)] = choose
        else:
            hand[hand.index(card)] = card_check(card)
    hand_count = count_cards(hand)
    return hand, hand_count


##Player rules: player can choose to draw more cards or stop. New cards will be checked again and the count will be done again.
def player_rules(player='Player'):
    player_cards, player_count = hand_rules(player)
    while True:
        print(f'The total hand is {player_count}.')
        print('-'*50)
        if player_count >= 21:
            break
        choose = input("Do you want to draw one more card? 'y' or 'n' ").lower()
        if choose == 'y':
            new_card = sort_cards()
            sleep(1)
            print(f'You draw {new_card}')
            new_card = card_check(new_card, 'Player')
            player_count+=new_card
            print(f'The {player} total hand is {player_count}.')
            print('-'*50)
        elif choose == 'n':
            print('The player has stopped.')
            break
        else:
            print('Choose e valid answer')
    return player_count


##Dealer Rules: Dealer will be the computer. Computer will choose how to treat Ace (11 if count <= 10, else 1).
def dealer_rules():
    dealer_cards, dealer_count = hand_rules()
    print(f'The total hand is {dealer_count}.')
    print('-'*50)
    while dealer_count <17:
        print('Drawing a new card...')
        new_card = sort_cards()
        sleep(2)
        print(f'Dealer draws {new_card}')
        new_card = card_check(new_card, pcount=dealer_count)
        dealer_count += new_card
        print(f'The Dealer total hand is {dealer_count}.')
        print('-'*50)
    print("The dealer has stopped.")
    return dealer_count

#Main_game will run each player function and check who won. Equal counts = Draw, 21 = Win, Over 21 = Lose. If both are below 21, the higher count wins.
def main_game():
    player = player_rules()
    sleep(3)
    computer = dealer_rules()
    if player == computer:
        print("It's a draw!")
    elif player == 21:
        print('Player wins.')
    elif computer == 21:
        print('Computer wins')
    elif player > 21:
        print('Computer wins.')
    elif computer > 21:
        print('Player wins.')
    else:
        if player > computer:
            print('Player wins')
        else:
            print('Computer Wins')
    while True:
        restart = input('Do you want to play again? ')
        if restart == 'n':
            BlackJack = False
            return BlackJack
        elif restart == 'y':
            display()
            main_game()
        else:
            print('Please type a valid answer.')


