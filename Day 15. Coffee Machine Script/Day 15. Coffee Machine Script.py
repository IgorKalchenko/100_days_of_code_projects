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
    "coffee": 100
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01
}

money = 0


def create_report():
    return "Water: {}ml\nMilk: {}ml\nCoffee: {}g\nMoney: ${}".format(
        resources["water"], resources["milk"],
        resources["coffee"], money
    )


def check_ingredients(drink):
    for ing in MENU[f"{drink}"]["ingredients"].keys():
        if resources[ing] < MENU[f"{drink}"]["ingredients"][ing]:
            print(f"Sorry there is not enough {ing}")
            return False
        resources[ing] -= MENU[f"{drink}"]["ingredients"][ing]
    return True


def asses_payment(price):
    print("Please insert coins.")
    inserted_sum = int(input("How many quarters?: ")) * coins["quarters"]
    inserted_sum += int(input("How many dimes?: ")) * coins["dimes"]
    inserted_sum += int(input("How many nickles?: ")) * coins["nickles"]
    inserted_sum += int(input("How many pennies?: ")) * coins["pennies"]
    if inserted_sum < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = inserted_sum - price
    global money
    money += price
    print(f"Here is ${change} in change.")
    return True


def main_logic():
    while True:
        answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if answer == "off":
            break
        if answer == "report":
            print(create_report())
            continue
        if not check_ingredients(answer):
            continue
        elif not asses_payment(MENU[answer]["cost"]):
            continue
        print(f"Here is your {answer} ☕.Enjoy!")


if __name__ == "__main__":
    main_logic()
