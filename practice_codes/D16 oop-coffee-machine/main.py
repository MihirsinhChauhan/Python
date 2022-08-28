from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem()


while True:
    options = input(f"What do you like? ({menu.get_items()}) ")
    if options == "report":
        money_machine.report()
        coffee_maker.report()
    elif options == "off":
        quit()
    else:
        drink = menu.find_drink(options)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
