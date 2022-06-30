import re
import os
from random import randint
from art import logo

card_list = list(range(2,11)) # list of cards 2-10
card_list.extend(['J','Q','K']) # add face cards to end of list
card_list.insert(0, 'A') # add ace to beginning of list
print(card_list)

def deal(deck: list) -> list:
    hand = []
    for deal in range(1,3):
        hand.append(deck[randint(0, len(deck) - 1)])
    return hand

def hit(deck: list, hand: list) -> list:
    # print(deck, hand)
    hand.append(deck[randint(0, len(deck) - 1)])
    return hand

def sum_hand(hand: list) -> int:
    hand_sum = 0
    for card in hand:
        if re.match("[AJQK]", str(card)):   # If card is a suit
            if re.match("[JQK]", card):
                hand_sum += 10
        else:                               # else card is a number
            hand_sum += int(card)
    ace_count = hand.count('A')
    if ace_count > 0:                       # Choosing A = 1 or 11
        if hand_sum > 10:
            hand_sum += ace_count
        else:
            hand_sum += 11
            if ace_count > 1:
                hand_sum += ace_count - 1

    return hand_sum            

def play_round(deck):
    os.system('clear')
    print(logo)
    
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print("Dealer: ", [dealer_hand[0], '_'])
    # print("Dealer: ", dealer_hand)
    print("Player: ", player_hand)

    # Check for Blackjack
    if sum_hand(player_hand) == 21 and sum_hand(dealer_hand) == 21:
        print("Player and dealer TIE")
        print(sum_hand(player_hand), sum_hand(dealer_hand))
    elif sum_hand(player_hand) == 21:
        print("BLACKJACK!!!")
        print(sum_hand(player_hand), sum_hand(dealer_hand))
    elif sum_hand(dealer_hand) == 21:
        print(dealer_hand)
        print("Dealer gets Blackjack, you lose this round.")
        print(sum_hand(player_hand), sum_hand(dealer_hand))
    else:
        player_lose = False
        dealer_lose = False
        # Players turn
        player_turn = True
        while player_turn:
            choice = input("Would you like to HIT or STAND? ").lower()
            if choice == 'stand' or choice == 's':
                player_turn = False
                player_score = sum_hand(player_hand)
                # print("Your score: ", player_score)
            elif choice == 'hit' or choice == 'h':
                player_hand = hit(deck, player_hand)
                print(player_hand)
                if sum_hand(player_hand) > 21:
                    player_turn = False
                    print("You busted.")
            else:
                print("Please instruct the dealer if you'd like to HIT or STAND")

        dealer_turn = True
        while dealer_turn:
            if sum_hand(player_hand) > 21:
                dealer_turn = False
            elif sum_hand(dealer_hand) < 16:
                dealer_hand = hit(deck, dealer_hand)
            else:
                dealer_turn = False
        
        dealer_score = sum_hand(dealer_hand)
        player_score = sum_hand(player_hand)
        print("Your score: ", player_score)
        print("Dealer: ", dealer_hand)
        print("Dealer's score: ", dealer_score)
        if player_score > 21:
            print("You Lose.")
        elif dealer_score > 21:
            print("You win... dealer busts")
        elif player_score > dealer_score:
            print("You WIN!!!")
        elif player_score == dealer_score:
            print("Player ties with dealer.")
        else:
            print("You Lose.")

    if input("Would you like to play again [y/n]? ") == 'y':
        play_round(deck)
                
            
play_round(card_list)