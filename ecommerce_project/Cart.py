"""Jack Reser
This program is an ecommerce store with a customer database and GUI
11/25/20"""


class Cart:
    """class Cart"""
    def __init__(self):
        self.item_list = []
        self.price_list = []

    # this method takes item information as parameters, and stores the name and price in separate lists
    def add_item(self, name, price):
        self.item_list.append(name)
        self.price_list.append(price)

    # this method adds up all the prices in the price_list, and returns the total
    def total_prices(self):
        total = 0
        for i in self.price_list:
            total += i
        return total

    # this method outputs a string containing each item separated by commas
    # each item consists of its name and price, pulled from their corresponding lists in the format (name : $price)
    def view_items(self):
        items = ""
        for i in range(len(self.price_list)):
            items += self.item_list[i] + " : $" + str("{:.2f}".format(self.price_list[i])) + ",  "
        return items

    # this method sets both the item_list and price_list equal to an empty list
    def empty_cart(self):
        self.item_list = []
        self.price_list = []
