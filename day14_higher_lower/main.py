import random
# from xmlrpc.client import boolean
import os
import art
from game_data import data

def get_data(data: dict) -> dict:
    return random.choice(data)

def entity_info(entity_data: dict) -> str:
    return f"{entity_data['name']}, a {entity_data['description']}, from {entity_data['country']}."

def entity_compare(entityA: dict, entityB: dict) -> bool:

    entityA_info = entity_info(entityA)
    entityB_info = entity_info(entityB)
    print(f"Compare A: {entityA_info}")
    print(art.vs)
    print(f"Compare B: {entityB_info}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == "A" and entityA['follower_count'] > entityB['follower_count']:
        print()
        return True
    elif choice == "B" and entityB['follower_count'] > entityA['follower_count']:
        print()
        return True
    else:
        print()
        return False

def play_game():
    playing = True
    score = 0
    comparison_list = [get_data(data), get_data(data)]
    while playing:
        os.system('clear')
        print(art.logo)

        if score > 0:
            print(f"You're right! Current score: {score}.")
            comparison_list = [entity_highest_followers, get_data(data)]

        entity_highest_followers = max(comparison_list, key=lambda x: x['follower_count']) # return dictionary in list with highest value of key 'follower_count'

        win_round = entity_compare(entityA = comparison_list[0], entityB = comparison_list[1])

        if win_round:
            score += 1
        else:
            playing = False
            os.system('clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()

