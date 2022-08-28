# from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
name = input("What's the name of Bidder? ")
amt = int(input("What's Bid amount $"))
bids = {}


def bid(bid_name, bid_amt):
    bids[bid_name] = bid_amt


bid(name, amt)
con = input("Is there other bidders also, Type 'yes' or 'no'\n")
while con == "yes":
    # clear()
    name = input("What's the name of Bidder? ")
    amt = int(input("What's Bid amount $"))
    bid(name, amt)
    con = input("Is there other bidders also, Type 'yes' or 'no'\n")
if con == "no":
    highest_bid = 0
    highest_bidder = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            highest_bidder = bidder

    print(f"Winner is {highest_bidder} with a bid of ${highest_bid}")
