import pandas as pd

alphabet_data = pd.read_csv('nato_phonetic_alphabet.csv')
user_word = list(input("Enter a word: ").upper())

alphabet = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}
output = [alphabet[char] for char in user_word]
print(output)