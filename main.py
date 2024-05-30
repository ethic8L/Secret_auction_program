import os

def clear_screen():
    # Check if the system supports terminal commands
    if os.getenv('TERM'):
        # Check if the system is Windows
        if os.name == 'nt':
            os.system('cls')
        # Else assume the system is Unix-based
        else:
            os.system('clear')
    else:
        print("\n" * 100)  # Print new lines to simulate clearing the screen



from art import logo
print(logo)

print("Welcome to secret auction program!")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders?: Type 'yes' or 'no': \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_screen()







