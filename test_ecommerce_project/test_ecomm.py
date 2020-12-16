import unittest
from ecommerce_project.Customer import Customer
from ecommerce_project.Cart import Cart


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cust = Customer("Jack", "Reser")
        self.cart = Cart()

    def tearDown(self):
        del self.cust
        del self.cart

    def test_customer_check_out(self):
        self.cust.cart.price_list = [10.34,44.33,7.99]
        self.assertEqual(round(self.cust.check_out(), 2), 67.05)

    def test_customer_name_output(self):
        self.assertEqual(self.cust.name_output(), "Reser, Jack")




if __name__ == '__main__':
    unittest.main()
