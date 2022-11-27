import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '^']
password_list = []
password = ''

print('Welcome to PyPassword Generator!')
num_of_letters = int(input('How many letters would you like in your password?\n'))
num_of_numbers = int(input('How many numbers would you like?\n'))
num_of_symbols = int(input('And how many special symbols would you like?\n'))

for let in range(0, num_of_letters):
    randomLetter = random.choice(letters)
    password_list.append(randomLetter)
for let in range(0, num_of_numbers):
    randomNumber = random.choice(numbers)
    password_list.append(randomNumber)
for let in range(0, num_of_symbols):
    randomSymbol = random.choice(symbols)
    password_list.append(randomSymbol)
#randomize the list order:
random.shuffle(password_list)
#generate password:
for char in password_list:
    password += char
    
print(f"Here is your password: {password} 💪")