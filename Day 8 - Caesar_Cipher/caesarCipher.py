from alphabet import *

print(logo)

def caesar(plain_text, shift_amount, cipher_direction):
    res = ''
    if cipher_direction in ('decode', 'd', 'D'):
        shift_amount *= -1
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = position + shift_amount
            res += alphabet[shifted_position]
        else:
            res += letter
    print(f"The {cipher_direction}d text: {res.upper()}")
        
over = False
while not over:
  direction = input("Type encode(E) to encrypt, type decode(D) to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(text, shift, direction)

  restart = input("Type yes(Y) if you want to go again. Otherwise type no(N).\n")
  if restart in ("no", 'N', 'n'):
    over = True
    print("Goodbye.")