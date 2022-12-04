# Read the rules in art.py
from art import logo
from replit import clear
import random as r

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    random_card = r.choice(cards)
    return random_card
     
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
        return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def compare(player_score, computer_score):
  if player_score > 21 and computer_score > 21:
    return "Busted. You Lose."
  if player_score == computer_score:
    return "Draw."
  elif computer_score == 0:
    return "You Lose. Computer has Blackjack"
  elif player_score == 0:
    return "Blackjack! You Won."
  elif player_score > 21:
    return "Busted. You lose."
  elif computer_score > 21:
    return "Computer Busted. You Win."
  elif player_score > computer_score:
    return "You Win."
  else:
    return "You Lose."

def blackjack():
    print(logo)

    game_over = False
    player_cards = []
    computer_cards = []
    
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {player_cards}, current score: {player_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
          game_over = True
        else:
            user_should_deal = input("Type 'yes(Y)' to deal another card, type 'No(N)' to pass: ")
            if user_should_deal in ['y', 'Y', 'yes']:
                player_cards.append(deal_card())
            else:
                game_over = True
    # Computer playing logic:
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"   Your final hand: {player_cards}, final score: {player_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    blackjack()