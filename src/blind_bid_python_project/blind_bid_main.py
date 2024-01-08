from art import logo
from clear import clear

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = int(0)
    winner = ""
    for bidder in bidding_record:
        bid_amount = int(bidding_record[bidder])
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?\n")
    price = input("What is your bid? $ \n")
    bids[name] = price
    should_continue = input("are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
