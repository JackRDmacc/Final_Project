"""Jack Reser
This program is an ecommerce store with a customer database and GUI
11/25/20"""

import tkinter
import datetime
from ecommerce_project import DB_Connector as db
from ecommerce_project import Customer


class ecomm_GUI:
    def __init__(self, window):
        self.customer = Customer.Customer("Guest", "Guest")
        self.cart_been_viewed = False
        self.viewing_customers = False

        self.conn = db.create_connection("customerDBMS.db")
        window.title("E-Commerce Order Process")
        window.geometry("600x700")

        self.l_instructions = tkinter.Label(window, text="Enter customer information, or just begin adding items to checkout as a guest.")
        self.l_instructions.pack()
        self.l_instructions2 = tkinter.Label(window, text="After checking out, empty your cart or enter new customer information to start a new purchase.")
        self.l_instructions2.pack()
        # ------
        self.b_add_customer = tkinter.Button(window, text="Add customer", command=lambda: self.add_customer())
        self.b_add_customer.pack()
        self.label_fname = tkinter.Label(window, text="First Name:")
        self.label_lname = tkinter.Label(window, text="Last Name:")
        self.e_fname = tkinter.Entry(window)
        self.e_lname = tkinter.Entry(window)
        self.label_fname.pack()
        self.e_fname.pack()
        self.label_lname.pack()
        self.e_lname.pack()
        # ------
        self.b_view_customers = tkinter.Button(window, text="View All Customers", command=lambda: self.view_customers())
        self.b_view_customers.pack()
        # ------
        self.l_table_data = tkinter.Label(window, text="")
        self.l_table_data.pack()
        # ------
        self.b_add_item = tkinter.Button(window, text="Add item to cart", command=lambda: self.add_item())
        self.b_add_item.pack()
        # ------
        self.label_name = tkinter.Label(window, text="Item Name:")
        self.label_price = tkinter.Label(window, text="Item Price:")
        self.e_item_name = tkinter.Entry(window)
        self.e_item_price = tkinter.Entry(window)

        self.label_name.pack()
        self.e_item_name.pack()
        self.label_price.pack()
        self.e_item_price.pack()
        # ------
        self.l_item_added = tkinter.Label(window, text="")
        self.l_item_added.pack()
        self.b_view_cart = tkinter.Button(window, text="Empty Cart", command=lambda: self.empty_cart())
        self.b_view_cart.pack()
        self.b_view_cart = tkinter.Button(window, text="View Cart", command=lambda: self.view_cart())
        self.b_view_cart.pack()
        self.l_cart_data = tkinter.Label(window, text="")
        self.l_cart_data.pack()
        # ------
        self.b_view_cart = tkinter.Button(window, text="Check Out", command=lambda: self.check_out())
        self.b_view_cart.pack()
        self.l_customer_name = tkinter.Label(window, text="")
        self.l_checkout_date = tkinter.Label(window, text="")
        self.l_cart_subtotal = tkinter.Label(window, text="")
        self.l_cart_tax = tkinter.Label(window, text="")
        self.l_cart_total = tkinter.Label(window, text="")
        self.l_customer_name.pack()
        self.l_checkout_date.pack()
        self.l_cart_subtotal.pack()
        self.l_cart_tax.pack()
        self.l_cart_total.pack()

    def add_customer(self):
        self.customer = Customer.Customer(self.e_fname.get(), self.e_lname.get())

        customer = (self.e_fname.get(), self.e_lname.get())
        customer_id = db.create_customer(self.conn, customer)
        self.conn.commit()
        self.b_add_customer.configure(state=tkinter.DISABLED)
        self.b_add_customer.configure(state=tkinter.NORMAL)
        self.e_lname.delete(0, tkinter.END)
        self.e_fname.delete(0, tkinter.END)

    def view_customers(self):
        if self.viewing_customers == False:
            rows = db.select_all_customers(self.conn)
            text = ""
            for row in rows:
                for col in row:
                    text += "{}     ".format(col)
                text += "\n"
            self.l_table_data.configure(text=text)
            self.viewing_customers = True
        else:
            self.l_table_data.configure(text="")
            self.viewing_customers = False

    def add_item(self):
        try:
            num = float(self.e_item_price.get())
            self.cart_been_viewed = False
            self.l_customer_name.configure(text="")
            self.l_cart_data.configure(text="")
            item_name = self.e_item_name.get()
            item_price = float(self.e_item_price.get())
            self.customer.cart.add_item(item_name, item_price)
            self.l_item_added.configure(text="Item Added: " + item_name + ", $" + str("{:.2f}".format(item_price)))
            self.e_item_name.delete(0, tkinter.END)
            self.e_item_price.delete(0, tkinter.END)
        except ValueError:
            self.l_item_added.configure(text="Invalid Input")
            self.e_item_name.delete(0, tkinter.END)
            self.e_item_price.delete(0, tkinter.END)

    def empty_cart(self):
        self.cart_been_viewed = False
        self.customer.cart.empty_cart()
        self.l_customer_name.configure(text="")
        self.l_item_added.configure(text="")
        self.l_cart_data.configure(text="")
        self.l_customer_name.configure(text="")
        self.l_checkout_date.configure(text="")
        self.l_cart_subtotal.configure(text="")
        self.l_cart_tax.configure(text="")
        self.l_cart_total.configure(text="")

    def view_cart(self):
        self.cart_been_viewed = True
        text = self.customer.cart.view_items()
        total = self.customer.cart.total_prices()
        output = text + "Cart Total: $" + "{:.2f}".format(total)
        self.l_cart_data.configure(text=output)

    def check_out(self):
        if (len(self.customer.cart.item_list) == 0):
            self.l_customer_name.configure(text="Please add an item to your cart")
        elif (self.cart_been_viewed):
            customer_output = "Customer: " + self.customer.name_output()
            date = "Purchase Date: " + str(datetime.datetime.now())
            subtotal_amt = self.customer.cart.total_prices()
            total_with_tax = self.customer.check_out()
            tax_amt = total_with_tax - subtotal_amt

            self.l_customer_name.configure(text=customer_output)
            self.l_checkout_date.configure(text=date)
            self.l_cart_subtotal.configure(text="Subtotal: $" + str("{:.2f}".format(subtotal_amt)))
            self.l_cart_tax.configure(text="Tax (7.00%): $" + str("{:.2f}".format(tax_amt)))
            self.l_cart_total.configure(text="Total: $" + str("{:.2f}".format(total_with_tax)))
        else:
            self.l_customer_name.configure(text="Please view cart before checking out")


app_window = tkinter.Tk()
ecomm_app = ecomm_GUI(app_window)
app_window.mainloop()
