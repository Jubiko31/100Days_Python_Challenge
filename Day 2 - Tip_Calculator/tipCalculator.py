print('Welcome to the tip calculator.')
total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("What percentage tip would you like to give? 5%, 10%, 15%? "))
# Check valid tip percantage:
if tip_percentage != 5 and tip_percentage != 10 and tip_percentage != 15:
    print('Invalid tip. Next time choose any valid option.')
else:
    number_of_persons = int(input("How many people to split the bill? "))
    amount_to_pay = (total_bill + total_bill * tip_percentage / 100) / number_of_persons
    price = round(amount_to_pay, 2)
    print(f"Each person should pay: ${price}")
