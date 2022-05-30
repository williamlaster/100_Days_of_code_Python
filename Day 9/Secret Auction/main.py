import os
import art

print(art.logo)

bids = {}
run_auction = False


def find_winning_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not run_auction:
    name = str(input("What is your name? : "))
    bid = int(input("What is your bid? : $"))
    bids[name] = bid
    auction_status = input("Are there anymore bidders? : ").lower()

    if auction_status == "no":
        run_auction = True
        find_winning_bidder(bids)
    elif auction_status == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
