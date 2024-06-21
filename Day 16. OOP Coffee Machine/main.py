from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()
while True:
    answer = input(f"What would you like? ({machine_menu.get_items()}): ").lower()
    if answer == "off":
        break
    if answer == "report":
        maker.report()
        money.report()
        continue
    your_drink = machine_menu.find_drink(answer)
    if not maker.is_resource_sufficient(your_drink):
        continue
    elif not money.make_payment(your_drink.cost):
        continue
    maker.make_coffee(your_drink)
