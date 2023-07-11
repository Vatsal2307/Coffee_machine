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
profit = 0


def is_sufficient(order_ingredients):
    """Checks if the ingredients are sufficient in resources as per order"""
    for item in order_ingredients:
        if order_ingredients[item] < resources[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}")
            return False


def process_coins():
    """Processes the input coins as per price range of the drinks"""
    print("Please insert coins")
    total = int(input("How many Quarters: ")) * 0.25
    total += int(input("How many Dimes: ")) * 0.1
    total += int(input("How many Nickel: ")) * 0.05
    total += int(input("How many Penny: ")) * 0.01
    return total


def transaction_success(entered_payment, drink_cost):
    """To check if transaction was success or not"""
    if entered_payment >= drink["cost"]:
        change = round(entered_payment - drink['cost'])
        print(f"Your change is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Transaction failed, Sorry that is not enough money.")
        return False


def make_coffee(drink_name, ordered_ingredients):
    """Makes ordered coffee once the transaction is checked successfully"""
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {user_input}, enjoy ☕️")


machine_on = True
while machine_on:
    user_input = input("What would you like to have? Espresso/Latte/Cappuccino :")
    if user_input == "off":
        machine_on = False
    elif user_input == "report":
        print(f"Water :{resources['water']}")
        print(f"Milk :{resources['milk']}")
        print(f"Coffee :{resources['coffee']}")
        print(f"Profit :{profit}")
    else:
        drink = MENU[user_input]
        if is_sufficient(drink['ingredients']):
            payment = process_coins()
            is_tran_success = transaction_success(payment, drink['cost'])
            if is_tran_success:
                make_coffee(user_input, drink['ingredients'])   
            else:
                print("Transaction failed, Here is your refund")
                machine_on = False
