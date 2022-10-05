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

coins_value = {
    "quarter": 0.25,
    "dimes": 0.10,
    "nickel": 0.25,
    "penny": 0.01,
}


# TODO: 4. Check resources sufficient
def check_resources_sufficient(coffee_type):
    for key in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][key] > resources[key]:
            print(f"Sorry, there is not enough {key}!")
            return False
    else:
        return True


# TODO: 3. Print report
def report():
    for key in resources:
        print(f"{key.capitalize()}: {'$' if key == 'money' else '' }{resources[key]}")


# TODO: 5. Process coins
def process_coins():
    tot = 0
    for coin in coins_value:
        tot += coins_value[coin] * float(input(f"how many {coin}?: "))
    return tot


def check_transaction_success(coffee, tot):
    price = MENU[coffee]["cost"]
    if price > tot:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if MENU[coffee]["cost"] < tot:
            print(f"Here is ${(tot - MENU[coffee]['cost'])} dollars in change.")
        return True


def make_the_coffee(coffee):
    if "money" in resources:
        resources["money"] += MENU[coffee]["cost"]
    else:
        resources["money"] = MENU[coffee]["cost"]
    for key in resources:
        if key != "money" and key in MENU[coffee]["ingredients"]:
            resources[key] -= MENU[coffee]["ingredients"][key]
    print(f"Enjoy your {coffee}")


# TODO: 1. Prompt user by asking which type of coffe she wants
choice = ""
total = 0

while choice != "off":
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "report":
        report()
    elif choice in MENU:
        total = process_coins()
        if check_resources_sufficient(choice) and check_transaction_success(choice, total):
            make_the_coffee(choice)
    elif choice == "off":
        exit()

# TODO: 6. Check transaction successful

# TODO: 7. Make a coffee
