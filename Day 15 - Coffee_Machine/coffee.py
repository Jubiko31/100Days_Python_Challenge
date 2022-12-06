from data import logo, MENU, resources

ON = True
profit = 0
menu = """
*-----------------------------------------------*
|            M      E      N      U             |
|-----------------------------------------------|
|   COFFEE   | PRICE | WATER | COFFEINE | MILK  |
|------------|-------|-------|----------|-------|
| Espresso   |  $1.5 | 50ml  |    18g   | 0ml   |
| Latte      |  $2.5 | 200ml |    24g   | 150ml |
| Cappuccino |  $3.0 | 250ml |    24g   | 100ml | 
|-----------------------------------------------|   
*-----------------------------------------------*
"""

def check_resource(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Not enough resources. Add some {ingredient}.")
            return False
    return True

def calculate_price():
    total = int(input("How many quarters? (1 qtr. = 25c.): ")) * 0.25
    total += int(input("How many dimes? (1 dm. = 10c.): ")) * 0.1
    total += int(input("How many nickles? (1 nk. = 5c.): ")) * 0.05
    total += int(input("How many pennies? (1 p. = 1c.): ")) * 0.01
    return total

def payment(money_paid, price):
    if money_paid >= price:
        change = round(money_paid - price, 2)
        print(f"Here is your change: ${change}.")
        global profit
        profit += price
        return True
    else:
        print("Not enough money. Money refunded.")
        return False

def make_coffee(cofe, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {cofe} ☕️. Enjoy!")

while ON:
    print(logo)
    print('Turn off the machine: "off"')
    print('Menu: type "bring me menu"')
    print('Enter "refil" to refil machine resources.')
    command = input("What would you like? (espresso/latte/cappuccino): ")
    if command == 'off':
        ON = False
    elif command == 'refil':
        resources["water"] = 300
        print('Refiled water container🌊')
        resources["milk"] = 200
        print('Refiled milk container🥛')
        resources['coffee'] = 100
        print('Coffee is full♨️')
    elif command == 'bring me menu':
        print(menu)
    elif command == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif command in ['espresso', 'latte', 'cappuccino']:
        coffee = MENU[command]
        is_resources = check_resource(coffee["ingredients"])
        if is_resources:
            price = calculate_price()
            pay = payment(price, coffee['cost'])
            if pay:
                make_coffee(command, coffee['ingredients'])
    else:
        ON = False
        print('We do not have that coffee. Bye.')

