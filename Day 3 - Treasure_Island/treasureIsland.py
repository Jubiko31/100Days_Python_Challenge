import time

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('You are at a cross road. Where do you want to go? Type "left" ⬅️  or "right" ➡️\n')

if direction == 'left':
    action = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" 🕒 to wait for a boat. Type "swim" 🌊 to swim across. Choice is yours...\n')
    if action == 'wait':
        print('Good you chose patience.')
        time.sleep(2)
        print('But it is not always good...')
        time.sleep(3)
        print('Just kidding, you made it. You arrive at the island unharmed.')
        time.sleep(1)
        print('Now final decesion...')
        time.sleep(1)
        final_decesion = input('There is a house with 3 doors🚪. One "red"🔺, one "white"⬜ and one "black"⚫. Which colour do you choose?\n')
        
        if final_decesion == 'black':
            print('Congrats. YOU ARE VICTORIUS!. 🎮')
        elif final_decesion == 'red':
            print('Burnt by Daenerys Targaryen. Game over. 🔥')
        elif final_decesion == 'white':
            print('You chose to code on light mode. Emotional damage. Game over. 🏳️')
        else:
            print('There was literally only three options! And you missed all. You are a failure. Game over.')
    else:
        print('Attacked by a crocodile🐊. Game over 👾')
else:
    print('You fall into a hole. Game over 👾')
    
