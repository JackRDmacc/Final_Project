"""Jack Reser
This program is an ecommerce store with a customer database and GUI
11/25/20"""
from ecommerce_project import Cart


class Customer:
    """class Customer"""
    next_id = 1000

    # Constructor
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.cust_id = self.next_id
        self.next_id += 1
        self.cart = Cart.Cart()

    def check_out(self):
        total = self.cart.total_prices()
        total = total * 1.07

        return total

    def name_output(self):
        name = self.lname + ", " + self.fname
        return name
