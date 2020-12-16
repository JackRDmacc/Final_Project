"""Jack Reser
This program is an ecommerce store with a customer database and GUI
11/25/20"""


class Cart:
    """class Cart"""
    def __init__(self):
        self.item_list = []
        self.price_list = []

    def add_item(self, name, price):
        self.item_list.append(name)
        self.price_list.append(price)

    def total_prices(self):
        total = 0
        for i in self.price_list:
            total += i
        return total

    def view_items(self):
        items = ""
        for i in range(len(self.price_list)):
            items += self.item_list[i] + " : $" + str("{:.2f}".format(self.price_list[i])) + ",  "
        return items

    def empty_cart(self):
        self.item_list = []
        self.price_list = []
