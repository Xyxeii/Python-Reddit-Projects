##Readme
#create a tuple of menu items with the price keyed with the order number
#get user input; account for spaces in the input
#calculate total order price as well as amount of that item ordered

import time
import enum
from collections import namedtuple, Counter

class Menu_Calc(object):
    def __init__(self, current_menu, order_number, order_code):
        self.current_menu = current_menu
        self.order_number = order_number
        self.order_code = order_code
        self.total_order_price = 0
        self.current_order = []
        for order in self.order_code:
            self.current_order.append(self.current_menu[order].name)
            self.total_order_price += self.current_menu[order].price

    def __repr__(self):
        return repr(self.order_number)

    def calculate_total(self):
        return f"{self.total_order_price:.2f}"

    def review_order(self):
        print("\nSo that will be: ")
        for menu_item, count in Counter(self.current_order).items():
            print(f"{count} {menu_item}")



class Create_Menu(object):
    def __init__(self, menu_items):
        Menu = namedtuple("Menu", ["name", "price"])
        self.menu_list = {}
        for item_id, key in enumerate(menu_items.keys(), 1):
            self.menu_list[str(item_id)] = Menu(name=key, price=menu_items[key])
        
    def __getitem__(self, order):
        return self.menu_list[order]

    def display_menu(self):
        for item in self.menu_list.keys():
            print("#{item_id}: {name} - ${price:.2f}".format(item_id = item, name = self.menu_list[item].name, price = self.menu_list[item].price))

menu_1 = {
    "Dave's Single": 5.19,
    "Dave's Double": 6.39,
    "Dave's Triple": 7.69,
    "Baconator": 7.09,
    "Son of Baconator": 5.29,
    "Spicy Chicken": 5.79,
    "Homestyle Chicken": 5.79,
    "Asiago Ranch Chicken Club": 6.79,
    "Ultimate Chicken Grill": 5.69,
    "10-pc Chicken Nuggets": 7.19,
    "Small Fries": 1.00,
    "Medium Fries": 1.50,
    "Large Fries": 2.00,
    "Small Drink": 1.00,
    "Medium Drink": 1.50,
    "Large Drink": 2.00,
    "Milk Shake": 3.25
}

dinner_menu = Create_Menu(menu_1)

# print(dinner_menu.display_menu())

# order1 = Menu_Calc(dinner_menu, 1, [12, 1, 3, 4])
# print(order1.calculate_total())
#dinner_menu[3].name

while True:
    order_number = 1
    current_menu = dinner_menu
    ready_to_order = input("\nHello, welcome to Wendy's!\n\nAre you ready to order? (y/n) ")
    if ready_to_order[0].lower() == 'y':
        print("\nHere is our menu:\n------------------------")
        current_menu.display_menu()
        user_order = input("\nGreat. What can I get for you? ")
        order = Menu_Calc(current_menu, order_number, user_order.split())
        order.review_order()
        print("\nYour total is ${}".format(order.calculate_total()))
        time.sleep(2)
        print("Thank you, Have a nice day.")
        time.sleep(2)
        order_number += 1
    else:
        print("\nOkay, have a nice day.")
        break