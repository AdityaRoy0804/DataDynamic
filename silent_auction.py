#This is an auction game .
#aditya Kumar Roy

import os

def winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price > highest_bid :
            highest_bid = bidding_price
            winner = bidder
    print(f"The winner is {winner} with bidding price {highest_bid}.")

bidder_data = {}
end = False
print("=========================")
print("Highest Bidder Wins...")
print("=========================")
while not end:
    name = input("What is your name ?")
    bid = int(input("Place your bid :"))
    bidder_data[name] = bid
    more_bid = input("Are there more bidders?(yes/no)").lower()
    if more_bid == "no":
        end = True
        winner(bidder_data)
    elif more_bid == "yes":
        os.system('cls')