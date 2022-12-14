PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        name_stripped = name.strip()
        new_letter = letter.replace(PLACEHOLDER, name_stripped)
        with open(f"./Output/ReadyToSend/letter_for_{name_stripped}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
