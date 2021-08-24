from os import system, name
from art import logo

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# is_stop = False
# bids = {}


# while not is_stop:
#     name = input("What is your name? ")
#     bid = int(input("What's your bid?: $"))
#     condition = input("Any other bider? Yes or no ").lower()

#     bids[name] = bid


#     if condition == "no":
#         is_stop = True

#     else:
#         clear()

# highest_bider = max(bids, key=bids.get)

# #### https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/

# print(f"The winner is {highest_bider} with a bid of ${bids[highest_bider]}")

##############################################################

#another way of doing it..



is_stop = False
bids = {}


def find_highest_bider(biders):
    highest_bid = 0
    winner = ""
    for biders_name in biders:
        bid_amount = bids[biders_name]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = biders_name

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not is_stop:
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    condition = input("Any other bider? Yes or no ").lower()

    bids[name] = bid

    if condition == "no":
        is_stop = True
        find_highest_bider(bids)

    elif condition == "yes":
        clear()