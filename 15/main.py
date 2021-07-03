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

# Cost of Coffee
COST_OF_ESPRESSO = config.MENU[ESPRESSO][COST]
COST_OF_LATTE = config.MENU[LATTE][COST]
COST_OF_CAPUCCINO = config.MENU[CAPPUCCINO][COST]

# Resource quantity required for different types of coffee
WATER_FOR_ESPRESSO = config.MENU[ESPRESSO][INGREDIENTS][WATER]
COFFEE_FOR_ESPRESSO = config.MENU[ESPRESSO][INGREDIENTS][COFFEE]
WATER_FOR_LATTE = config.MENU[LATTE][INGREDIENTS][WATER]
COFFEE_FOR_LATTE = config.MENU[LATTE][INGREDIENTS][COFFEE]
MILK_FOR_LATTE = config.MENU[LATTE][INGREDIENTS][MILK]
WATER_FOR_CAPUCCINO = config.MENU[CAPPUCCINO][INGREDIENTS][WATER]
COFFEE_FOR_CAPUCCINO = config.MENU[CAPPUCCINO][INGREDIENTS][COFFEE]
MILK_FOR_CAPUCCINO = config.MENU[CAPPUCCINO][INGREDIENTS][MILK]


def get_resources():
    print(f"Water: {water}\nMilk:  {milk}\nCoffee:{coffee}\nMoney: ${money}")


def select_from_menu():
    selected_item = input(f"What would you like to order?({ESPRESSO}/{LATTE}/{CAPPUCCINO}):")
    return selected_item


def is_resources_sufficient(coffee_type):
    is_sufficient = False
    water_insufficient_message = "Sorry there is not enough water."
    coffee_insufficient_message = "Sorry there is not enough coffee."
    milk_insufficient_message = "Sorry there is not enough milk."
    if coffee_type == ESPRESSO:
        if water < 50:
            print(water_insufficient_message)
        elif coffee < 18:
            print(coffee_insufficient_message)
        else:
            is_sufficient = True
    elif coffee_type == LATTE:
        if water < 200:
            print(water_insufficient_message)
        elif coffee < 24:
            print(coffee_insufficient_message)
        elif milk < 150:
            print(milk_insufficient_message)
        else:
            is_sufficient = True
    else:
        if water < 250:
            print(water_insufficient_message)
        elif coffee < 24:
            print(coffee_insufficient_message)
        elif milk < 100:
            print(milk_insufficient_message)
        else:
            is_sufficient = True
    return is_sufficient


def ask_money():
    print("Please insert coins.")
    penny = int(input("How many penny?"))
    nickel = int(input("How many nickel?"))
    dime = int(input("How many dime?"))
    quarter = int(input("How many quarter?"))

    total = penny*0.01 + nickel*0.05 + dime*0.1 + quarter*0.25

    return total


def is_money_sufficient(coffee_type, money_received):
    is_sufficient = False
    money_insufficient_message = "Sorry, that's not enough money. Money Refunded."
    if coffee_type == ESPRESSO:
        if money_received < COST_OF_ESPRESSO:
            print(money_insufficient_message)
        else:
            is_sufficient = True
    elif coffee_type == LATTE:
        if money_received < COST_OF_LATTE:
            print(money_insufficient_message)
        else:
            is_sufficient = True
    else:
        if money_received < COST_OF_CAPUCCINO:
            print(money_insufficient_message)
        else:
            is_sufficient = True
    return is_sufficient


def prepare_change(coffee_type, money_received):
    global money
    customer_paid = float(money_received)
    if coffee_type == ESPRESSO:
        customer_change = round(customer_paid - COST_OF_ESPRESSO, 2)
        money += COST_OF_ESPRESSO
        print(f"Here is ${customer_change} in change.")
    elif coffee_type == LATTE:
        customer_change = round(customer_paid - COST_OF_LATTE, 2)
        money += COST_OF_LATTE
        print(f"Here is ${customer_change} in change.")
    else:
        customer_change = round(customer_paid - COST_OF_CAPUCCINO, 2)
        money += COST_OF_CAPUCCINO
        print(f"Here is ${customer_change} in change.")


def use_resources(water_quantity, coffee_quantity, milk_quantity):
    global water
    global coffee
    global milk
    water -= int(water_quantity)
    coffee -= int(coffee_quantity)
    milk -= int(milk_quantity)


def prepare_coffee(coffee_type):
    if coffee_type == ESPRESSO:
        use_resources(WATER_FOR_ESPRESSO, COFFEE_FOR_ESPRESSO, 0)
        print(f"Here is your {coffee_type} ☕. Enjoy")
    elif coffee_type == LATTE:
        use_resources(WATER_FOR_LATTE, COFFEE_FOR_LATTE, MILK_FOR_LATTE)
        print(f"Here is your {coffee_type} ☕. Enjoy")
    else:
        use_resources(WATER_FOR_CAPUCCINO, COFFEE_FOR_CAPUCCINO, MILK_FOR_CAPUCCINO)
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
