from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    options = menu.get_items()
    selection = input(f"What would you like? ({options}): ")

    if selection == 'off':
        machine_on = False
    elif selection == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(selection)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


