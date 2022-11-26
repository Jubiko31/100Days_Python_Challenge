# Classical Rock Paper Scissors game agains computer
import random as r
# ASCII for visuals:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [0,1,2]
game_images = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors game!")
# decisions
human_choice = int(input("What do you choose? Enter 0 for ROCK⛰️, 1 for PAPER📜 and 2 for SCISSORS✂️ \n"))
computer_choice = r.randint(0, 2)
#validation
if human_choice not in options:
    print('Well done. You cannot even choose valid option.')
    print('You Lose.')
    print('Reason: FAILURE')
else:
    print(game_images[human_choice])
    print("Computer chose:")
    print(game_images[computer_choice])
    # Finisher Condtions:
    if computer_choice >= 2 and human_choice == 0:
        print('YOU WIN! 🏁')
    elif computer_choice == 0 and human_choice == 2:
        print('You Lose. ❌')
    elif computer_choice > human_choice:
        print('You Lose. ❌')
    elif computer_choice < human_choice:
        print('YOU WIN! 🏁')
    else:
        print('Draw.')