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
    "money": 0.0,
}

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01


def check_resources(drink):
    """Checks if there are enough resources to make the choosen drink"""
    for key in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][key] > resources[key]:
            print(f"{key} too low, please refill")
            return
    print("Please insert coins")
    num_quarters = int(input("how many quarters?: "))
    num_dimes = int(input("how many dimes?: "))
    num_nickels = int(input("how many nickels?: "))
    num_pennies = int(input("how many pennies?: "))

    total = num_quarters * quarter + num_dimes * \
        dime + num_nickels * nickel + num_pennies * penny

    if total == MENU[drink]["cost"]:
        resources["money"] += total
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        print(f"Here is you {drink}. Enjoy!")
    elif total > MENU[drink]["cost"]:
        resources["water"] -= MENU[drink]["ingredients"]["water"]
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
        resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
        change = total - MENU[drink]["cost"]
        total -= change
        resources["money"] += total
        print(f"Here is ${change} in change")
        print(f"Here is you {drink}. Enjoy!")
    else:
        print("Sorry that was not enough money. Money refunded.")


def proccess_user_choice():
    run = True
    while run:
        # Prompt user for what they want (hidden "off", "report", and "refill" commands)
        user_choice = input(
            "What would you like? (| espresso | latte | cappuccinn |): ").lower()
        # If user choice is "off" end the program
        if user_choice == "off":
            run = False
            return run
        elif user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif user_choice == "refill":
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
        elif user_choice == "espresso" or "latte" or "cappuccino":
            check_resources(user_choice)
        else:
            run = False
            return run


proccess_user_choice()
