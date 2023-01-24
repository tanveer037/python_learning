Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            'milk': 0
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
    'money': 0
}


def check_resources(coffee_type):
    compare_items = list(
        Menu[coffee_type]['ingredients'].keys()
    )
    return all(
        Menu[coffee_type]['ingredients'].get(item) <= resources.get(item) for item in compare_items
    )


def process_coin():
    valid_coins = {
        'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01
    }
    inserted_coins = list(input("Enter coins: ").split())
    # 1 quarters 2 dimes = [('1' = x, 'quarters' = y), (2, dimes)] = [0.25, 0.20] = 0.45
    it = iter(inserted_coins)
    coins_tuple = list(zip(it, it))
    coins_value = [(int(x) * valid_coins[y]) for x, y in coins_tuple]
    total_value = sum(coins_value)
    return total_value


def check_transaction(coffee_type):
    total = process_coin()
    if total < Menu[coffee_type]['cost']:
        print("Sorry that's not enough money.Money refunded")
        return False
    elif total >= Menu[coffee_type]['cost']:
        if total > Menu[coffee_type]['cost']:
            change = total - Menu[coffee_type]['cost']
            resources['money'] += Menu[coffee_type]['cost']
            print(f"Here is ${change} dollars in change")
        else:
            resources['money'] += Menu[coffee_type]['cost']
        return True


def make_coffee(coffee_type):
    if check_resources(coffee_type):
        resources["water"] -= Menu[coffee_type]['ingredients']['water']
        resources["coffee"] -= Menu[coffee_type]['ingredients']['coffee']
        resources["milk"] -= Menu[coffee_type]['ingredients']['milk']
        print(f"Here is your {coffee_type}. Enjoy!")
    else:
        if resources["water"] < Menu[coffee_type]['ingredients']['water'] and resources["coffee"] < Menu[coffee_type]['ingredients']['coffee'] and resources["milk"] < Menu[coffee_type]['ingredients']['milk']:
            print("Sorry, there is not enough water, coffee and milk")
        elif resources["water"] < Menu[coffee_type]['ingredients']['water'] and resources["coffee"] < Menu[coffee_type]['ingredients']['coffee']:
            print("Sorry there is not enough water and coffee")
        elif resources["water"] < Menu[coffee_type]['ingredients']['water'] and resources["milk"] < Menu[coffee_type]['ingredients']['milk']:
            print("Sorry there is not enough water and milk")
        elif resources["coffee"] < Menu[coffee_type]['ingredients']['coffee'] and resources["milk"] < Menu[coffee_type]['ingredients']['milk']:
            print("Sorry there is not enough coffee and milk")
        elif resources["water"] < Menu[coffee_type]['ingredients']['water']:
            print("Sorry there is not enough water")
        elif resources["coffee"] < Menu[coffee_type]['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
        elif resources["milk"] < Menu[coffee_type]['ingredients']['milk']:
            print("Sorry there is not enough milk")


def order():
    choice = input('What would you like? (espresso/latte/cappucino): ')
    while choice != 'off':
        if choice == 'espresso':
            if check_transaction('espresso'):
                make_coffee('espresso')
        elif choice == 'latte':
            if check_transaction('latte'):
                make_coffee('espresso')
        elif choice == 'cappucino':
            if check_transaction('cappucino'):
                make_coffee('cappucino')
        elif choice == 'report':
            print(resources)
        else: print('Not available!')
        choice = input('What would you like? (espresso/latte/cappucino): ')

order()

