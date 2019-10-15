##Readme
#create a tuple of menu items with the price keyed with the order number
#get user input; account for spaces in the input
#calculate total order price as well as amount of that item ordered

import time
from collections import namedtuple, Counter

class Menu_Calc(object):
    def __init__(self, current_menu, order_number):
        self.current_menu = current_menu
        self.order_number = order_number
        self.total_order_price = 0
        self.current_order = []


    def __repr__(self):
        return repr(self.order_number)

    def add_item(self, item_id):
        self.current_order.append(self.current_menu[item_id].name)
        self.total_order_price += self.current_menu[item_id].price
        if item_id[:2] == "me":
            while True:
                make_combo = input("\nWould you like to make that a combo? (y/n) ")
                if make_combo[0].lower() == "y":
                    self.add_combo(item_id)
                    return
                elif make_combo[0].lower() == "n":
                    return
                else:
                    print("I'm sorry I don't understand?")

    def add_combo(self, item_id):
        while True:
            combo_size = input("What size would you like? (s/m/l) ")
            if combo_size[0].lower() == "s":
                self.add_item("si1")
                self.add_item("dr1")
                return
            elif combo_size[0].lower() == "m":
                self.add_item("si2")
                self.add_item("dr2")
                return
            elif combo_size[0].lower() == "l":
                self.add_item("si3")
                self.add_item("dr3")
                return
            else:
                print("I'm sorry I don't understand.")

    def calculate_total(self):
        return f"{self.total_order_price:.2f}"

    def review_order(self):
        print("\nSo that will be: ")
        for menu_item, count in Counter(self.current_order).items():
            print(f"{count} {menu_item}")



class Create_Menu(object):
    def __init__(self, menu_items):
        self.menu_list = {}
        for categories, items in menu_items.items():
            Menu = namedtuple(categories, ["name", "price"])
            for item_id, key in enumerate(items.keys(), 1):
                self.menu_list[categories[0:2].lower() + str(item_id)] = Menu(name=key, price=items[key])
        print(self.menu_list)
        
    def __getitem__(self, item_id):
        try:
            return self.menu_list[item_id]
        except KeyError:
            return self.menu_list[str(item_id)]

    def display_menu(self):
        ##DO THIS WITHOUT A FOR LOOP THANKS
        for category, items in self.menu_list.items():
            if category[:2] == "me":
                print("#{item_id}: {name} - ${price:.2f}".format(item_id = category[2:], name = items.name, price = items.price))
            else:
                print("{name} - ${price:.2f}".format(name = items.name, price = items.price))

menu_1 = {
    "Meals":{
        "Dave's Single": 5.19,
        "Dave's Double": 6.39,
        "Dave's Triple": 7.69,
        "Baconator": 7.09,
        "Son of Baconator": 5.29,
        "Spicy Chicken": 5.79,
        "Homestyle Chicken": 5.79,
        "Asiago Ranch Chicken Club": 6.79,
        "Ultimate Chicken Grill": 5.69,
        "10-pc Chicken Nuggets": 7.19
    },

    "Sides":{
        "Small Fries": 1.00,
        "Medium Fries": 1.50,
        "Large Fries": 2.00,
    },

    "Drinks":{
        "Small Drink": 1.00,
        "Medium Drink": 1.50,
        "Large Drink": 2.00,
        "Milk Shake": 3.25
    }
}

dinner_menu = Create_Menu(menu_1)
# order = Menu_Calc(dinner_menu, 1)
# order.add_item("me5")

# dinner_menu.display_menu()


while True:
    order_number = 1
    restaurant_name = "Wendy's"
    current_menu = dinner_menu
    print(f"\nHello, welcome to {restaurant_name}!\n\nHere is our menu:\n------------------------")
    current_menu.display_menu()
    user_order = []
    order = Menu_Calc(current_menu, order_number)
    initial_order = True
    while True:
            customer_item = input("\nWhat can I get for you? ")
            order.add_item(customer_item)
            another_order = input("\nWould you like anything else? ")
            if another_order[0].lower() == 'y':
                pass
            elif another_order[0].lower() == 'n':
                break
            else:
                print("I'm sorry I don't understand?")
    print(f"\nOrder Number: {order_number}")
    order.review_order()
    print("\nYour total is ${}".format(order.calculate_total()))
    time.sleep(2)
    print("Thank you, Have a nice day.")
    order_number += 1
    time.sleep(5)
