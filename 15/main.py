import config

# Variable Constants
REPORT = "report"
SWITCH_OFF = "off"
ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"
INGREDIENTS = "ingredients"
WATER = "water"
COFFEE = "coffee"
MILK = "milk"
COST = "cost"

# Resources
water = config.resources[WATER]     # ml
milk = config.resources[MILK]       # ml
coffee = config.resources[COFFEE]   # g
money = 0.0                         # $


def get_resources():
    print(f"Water: {water}\nMilk:  {milk}\nCoffee:{coffee}\nMoney: ${money}")


def select_from_menu():
    selected_item = input(f"What would you like to order?({ESPRESSO}/{LATTE}/{CAPPUCCINO}):")
    return selected_item


def is_resources_sufficient(coffee_type):
    selected_coffee_ingredients = config.MENU[coffee_type][INGREDIENTS]
    resources = config.resources
    for ingredient in selected_coffee_ingredients:
        if selected_coffee_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def ask_money():
    print("Please insert coins.")
    penny = int(input("How many penny?"))
    nickel = int(input("How many nickel?"))
    dime = int(input("How many dime?"))
    quarter = int(input("How many quarter?"))

    total = penny*0.01 + nickel*0.05 + dime*0.1 + quarter*0.25

    return total


def is_money_sufficient(coffee_type, money_received):
    coffee_types = config.MENU
    money_insufficient_message = "Sorry, that's not enough money. Money Refunded."
    for coffee in coffee_types:
        if coffee_type == coffee:
            if money_received < coffee_types[coffee][COST]:
                print(money_insufficient_message)
                return False
            else:
                return True


def prepare_change(coffee_type, money_received):
    global money
    customer_paid = float(money_received)
    coffee_types = config.MENU

    for coffee in coffee_types:
        if coffee_type == coffee:
            cost_of_coffee = coffee_types[coffee][COST]
            customer_change = round(customer_paid - cost_of_coffee, 2)
            money += cost_of_coffee
            print(f"Here is ${customer_change} in change.")


def use_resources(water_quantity, coffee_quantity, milk_quantity):
    global water
    global coffee
    global milk
    water -= int(water_quantity)
    coffee -= int(coffee_quantity)
    milk -= int(milk_quantity)


def prepare_coffee(coffee_type):
    coffee_types = config.MENU
    if coffee_type == ESPRESSO:
        use_resources(
            coffee_types[coffee_type][INGREDIENTS][WATER],
            coffee_types[coffee_type][INGREDIENTS][COFFEE],
            0
        )
        print(f"Here is your {coffee_type} ☕. Enjoy")
    else:
        use_resources(
            coffee_types[coffee_type][INGREDIENTS][WATER],
            coffee_types[coffee_type][INGREDIENTS][COFFEE],
            coffee_types[coffee_type][INGREDIENTS][MILK]
        )
        print(f"Here is your {coffee_type} ☕. Enjoy")


def order_coffee(coffee_type):
    is_resource_enough = bool(is_resources_sufficient(item))
    if is_resource_enough:
        money_received = ask_money()
        is_money_enough = bool(is_money_sufficient(coffee_type, money_received))
        if is_money_enough:
            prepare_change(coffee_type, money_received)
            prepare_coffee(coffee_type)


is_on = True
while is_on:
    item = select_from_menu()
    if item == REPORT:
        get_resources()
    elif item == SWITCH_OFF:
        is_on = False
    else:
        order_coffee(item)
