from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while on:
    options = menu.get_items()
    print(' \nTurn off: "off"')
    print('Menu: "menu"')
    print('Report: report')
    command = input(f"What would you like? ({options}): ")
    if command == 'off':
        on = False
    elif command == 'menu':
        print("Latte => $2.5\nEspresso => $1.5\nCappuccino => $3.0")
    elif command == 'report':
        coffee_maker.report()
        money_machine.report()
    elif command in ['espresso', 'latte', 'cappuccino']:
        drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print('Please choose coffee from menu, not from your imagination.')