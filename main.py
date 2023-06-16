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
    "money": 0,
}


def print_report():
    """Prints out an inventory of resources"""
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")


def resources_available():
    """Returns True if there is enough resources to make and False if not"""
    for ingredient in MENU[answer]['ingredients']:
        if MENU[answer]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True


def process_payment():
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * .25
    total += int(input("How many dimes?: ")) * .1
    total += int(input("How many nickles?: ")) * .05
    total += int(input("How many pennies?: ")) * .01
    return total


def enough_money():
    """Returns True if customer gave enough money and False if not"""
    if payment < MENU[answer]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return True


power = True
while power:
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "off":
        power = False
    elif answer == "report":
        print_report()
    else:
        if resources_available():
            payment = process_payment()
            if enough_money():
                resources['money'] += MENU[answer]['cost']
                if payment > MENU[answer]['cost']:
                    print(f"Here is ${(payment - MENU[answer]['cost']):.2f} in change.")
                for item in MENU[answer]['ingredients']:
                    resources[item] -= MENU[answer]['ingredients'][item]
                print(f"Here is your {answer}. ENJOY!!!")
