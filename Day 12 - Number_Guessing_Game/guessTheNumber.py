from art import logo
from random import randint

def choose_difficulty():
  level = input("Choose a difficulty. Type 'eazy(E)' or 'hard(H)': ")
  if level in ('eazy', 'e', 'E'):
    return 10
  else:
    return 5

def check_guess(guess, answer, turns):
    if guess > answer:
        print('Too high 🌿')
        return turns - 1
    elif guess < answer:
        print('Too low 🧊')
        return turns - 1
    else:
        print(f"Hah, You got it! The answer was {answer}.")

def guessTheNumber():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    answer = randint(1, 100)
    guess = 0

    print("I'm thinking of a number between 1 and 100...💭")
    turns = choose_difficulty()
        
    while guess != answer:    
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input('Make a guess: '))
        turns = check_guess(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, You Lose.")
            return
        elif guess != answer:
            print("Guess again.")
        
guessTheNumber()