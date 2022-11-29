# Classic Hangman game in Python
import random
from ui import *
from wordlist import *

print(logo)

game_over = False
display = []
note = ''
lives = 6

chosen = random.choice(wordlist)
word_length = len(chosen)
for _ in range(word_length):
    display += "_"

while not game_over:
    print(stages[lives])
    guess = input('Guess a letter: ').lower()
    # if player asked for hint:
    print('If you want hint type - "hint"')
    if guess == 'hint':
        print(f"Hint💡: {notes[wordlist.index(chosen)]}")
    elif guess not in chosen:
        lives -= 1
    else:
        for position in range(0, len(chosen)):
            letter = chosen[position]
            if letter == guess:   
                display[position] = letter
    print(f"{' '.join(display)}")

    if '_' not in display:
        print('You Won!🏆')
        game_over = True
        
    if lives == 0:
        print(stages[0])
        print('You have been hanged.☠️')
        game_over = True