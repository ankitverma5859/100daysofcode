from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

# Variable Constants
REPORT = "report"
SWITCH_OFF = "off"


def select_from_menu():
    menu_items = menu.get_items()
    selected_item = input(f"What would you like to order?({menu_items}):")
    return selected_item


def order_coffee(coffee_type):
    is_resource_enough = coffee_maker.is_resource_sufficient(coffee_type)
    if is_resource_enough:
        is_money_enough = money_machine.make_payment(coffee_type.cost)
        if is_money_enough:
            coffee_maker.make_coffee(coffee_type)


is_on = True
while is_on:
    item = select_from_menu()
    if item == REPORT:
        coffee_maker.report()
        money_machine.report()
    elif item == SWITCH_OFF:
        is_on = False
    else:
        drink = menu.find_drink(item)
        if drink is not None:
            order_coffee(drink)
