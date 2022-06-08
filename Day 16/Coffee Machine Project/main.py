from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


jeff = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True


while is_on:
    options = menu.get_items()
    user_order = input(
        f"What would you like to order {options}: ").lower()
    if user_order == "report":
        jeff.report()
        money_machine.report()
    elif user_order == "off":
        is_on = False
    else:
        ordered_item = menu.find_drink(user_order)

    if jeff.is_resource_sufficient(ordered_item) and money_machine.make_payment(ordered_item.cost):
        jeff.make_coffee(ordered_item)
