from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

menu_choice = input(f"What the hell you wat to drink? {menu.get_items()} : ")
while menu_choice != "off":
    if menu_choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        menu_item = menu.find_drink(menu_choice)
        if menu_item and coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)
            print("Enjoy your order !")
    menu_choice = input(f"What the hell you wat to drink? {menu.get_items()}")