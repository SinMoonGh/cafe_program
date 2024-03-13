from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# menu = Menu()
menu_item = MenuItem("라떼", 100, 100, 55, 3.5)

print(menu_item.ingredients['water'])

menu =Menu()
#print(menu.menu[menu.find_drink('latte')].cost)
drink = menu.find_drink(order_name='latte')
print(drink.cost)