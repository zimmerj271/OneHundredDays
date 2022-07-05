MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickels": 0.05,
    "pennies": 0.01,
}

bank = 0  # amount of money in the coffee machine


def get_report():
    for item in resources:
        if item == 'water' or item == 'milk':
            print(f"{item}: {resources[item]}ml")
        else:
            print(f"{item}: {resources[item]}mg")
    print(f"Money: ${bank}")


def get_menu():
    for item in MENU:
        print(f"{item}: ${MENU[item]['cost']}")


def check_resources(menu_item: dict) -> dict:
    # input menu_item should be in format MENU['latte']['ingredients']
    resource_check = {}
    for ingredient in menu_item:
        if menu_item[ingredient] > resources[ingredient]:
            resource_check[ingredient] = False
        else:
            resource_check[ingredient] = True
    return resource_check


def make_drink(menu_item: str):
    print(f"Making {menu_item}")
    for ingredient in MENU[menu_item]['ingredients']:
        resources[ingredient] -= MENU[menu_item]['ingredients'][ingredient]


def get_money() -> dict:
    def get_coin(coin: str, coin_dict: dict):
        coin_input = ''
        while not coin_input.isnumeric():
            coin_input = input(f"how many {coin}? ")
            if coin_input == 'report':
                get_report()
            elif coin_input == 'menu':
                get_menu()

        coin_dict[coin] = int(coin_input)

    quarters = dimes = nickels = pennies = ''
    user_coins = {
        "quarters": '',
        "dimes": '',
        "nickels": '',
        "pennies": '',
    }
    print("Please insert coins")
    for coin in user_coins:
        get_coin(coin, user_coins)

    return user_coins


def process_money(coins: dict) -> bool:
    amount = 0
    for coin in coins:
        if coin == 'quarters':
            amount += 0.25 * coins[coin]
        elif coin == 'dimes':
            amount += 0.1 * coins[coin]
        elif coin == 'nickels':
            amount += 0.05 * coins[coin]
        elif coin == 'pennies':
            amount += 0.01 * coins[coin]
        else:
            amount = 'ERROR'

    return amount


def get_change(money: float, item: str) -> float:
    return money - MENU[item]['cost']


def check_input(user_input: str):
    if user_input == 'off':
        return True
    elif user_input == 'report':
        get_report()
        # return False
    elif user_input == 'menu':
        get_menu()
        # return False
    # else:
    #     return False
    return False


def coffee_machine():
    global bank
    machine_on = True
    while machine_on:
        selection = ''
        while not (selection == "latte" or selection == "espresso" or selection == 'cappuccino'):
            selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if check_input(selection) == 'off':
                machine_on = False
                break

        resource_check = check_resources(MENU[selection]['ingredients'])
        not_enough_resources = None
        for ingredient in resource_check:
            if not resource_check[ingredient]:
                not_enough_resources = ingredient
                break
        if not_enough_resources:
            print(f"Sorry, there is not enough {not_enough_resources}")
            continue

        if machine_on:
            money = get_money()
            money_amount = process_money(money)
            print(f"You gave ${money_amount}")
            if money_amount < MENU[selection]['cost']:
                print("Sorry that's not enough money. Money refunded.")
                continue
            else:
                make_drink(selection)
                bank += money_amount
                money_change = get_change(money_amount, selection)
                print(f"Here is ${money_change} in change.")
                print(f"Here is your {selection} ☕. Enjoy!")




coffee_machine()