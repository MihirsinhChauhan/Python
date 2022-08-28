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


def menu():
    global resources
    menu = input("What do you want? (espresso/latte/cappuccino) ").lower()
    if menu == "report":
        for key in resources:
            print(key, " : ", resources[key])
    elif menu == "off":
        quit()
    return menu


def check(hot_flavour):
    global MENU
    for ingredient in MENU[hot_flavour]["ingredients"]:
        if resources[ingredient] > MENU[hot_flavour]["ingredients"][ingredient]:
            ing_available = True

        else:
            print(f"Sorry there is not enough {ingredient}")
            return 0
    return ing_available


def transaction(hot_flavour):
    print("Please insert coins.")
    quarters = float(input("how many quarters? "))
    dimes = float(input("how many dimes? "))
    nickles = float(input("how many nickles? "))
    pennies = float(input("how many pennies? "))
    money_given = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    global MENU
    if MENU[hot_flavour]["cost"] > money_given:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        change = round(money_given - MENU[hot_flavour]["cost"], 2)
        print(f"Here is ${change} dollars in change")
        return 1


def make_coffee(hot_flavour):
    global MENU
    global resources

    for ingredient in resources:
        remaining_vol = resources[ingredient] - MENU[hot_flavour]["ingredients"][ingredient]
        resources[ingredient] = remaining_vol
    print(f"Here is your {hot_flavour}. Enjoy!")


while True:
    flavour = menu()
    if flavour == "report":
        continue
    check_resources = check(flavour)
    if check_resources == 0:
        continue
    elif check_resources:
        check_transaction = transaction(flavour)
        if check_transaction == 0:
            continue
        elif check_transaction:
            make_coffee(flavour)
