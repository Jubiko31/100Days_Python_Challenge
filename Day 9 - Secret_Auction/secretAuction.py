from replit import clear
from art import introduction

introduction()

participants = {}
auction_over = False

def find_highest_bidder(bidders):
    highest = 0
    winner = ""
    for bidder in bidders:
        tmp = bidders[bidder]
        if tmp > highest:
            highest = tmp
            winner = bidder
    
    print(f"Three, two, one and sold!\nWinner is {winner} with the highest bid: ${highest}")
    

while not auction_over:
    name = input('What is your name? ')
    bid = int(input('What is your bid? $'))
    participants[name] = bid
    
    is_continue = input('Are there any other bidder? Type yes(Y) or no(N)? ')
    if is_continue in ('N', 'n', 'no'):
        auction_over = True
        find_highest_bidder(participants)
    elif is_continue in ('Y', 'y', 'yes'):
        clear()
    else:
        print('There is literally two options. Come on you can do it better. ')