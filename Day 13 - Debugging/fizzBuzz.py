# Assignment to Debug:
# for number in range(1, 101):
#     if number % 3 == 0 or number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print("Fizz")
#     if number % 5 == 0:
#         print("Buzz")
#     else:
#         print([number])

# Correct version:
for number in range(1, 101):
    print(f"Currently checking number {number}")
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)