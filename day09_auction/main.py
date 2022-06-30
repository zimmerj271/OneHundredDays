import os
from art import logo

clear = lambda: os.system('clear')
def get_winning_bid(bidding_dict):
    max_value = 0
    name = ''
    for bidder in bidding_dict:
        bid = bidding_dict[bidder]
        if bid > max_value:
            max_value = bid
            name = bidder
    
    winner = {"name": name, "bid": max_value}

    return winner

print(logo)

bids = {}
bidding = True
while bidding:
    name = input("What is the name of the bidder? ")
    price = int(input("What is the bid price? $"))

    bids[name] = price

    continue_bidding = input("Are there any other bidders [yes/no]? ")
    if continue_bidding == 'no':
        bidding = False
        highest_bid = get_winning_bid(bids)
        print(f"The winner is {highest_bid['name']}, who bid {highest_bid['bid']}!")
    else:
        clear()
