"""Jack Reser
This program is an ecommerce store with a customer database and GUI
11/25/20"""

import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(conn):

    sql_create_customer_table = """ CREATE TABLE IF NOT EXISTS customer (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    # create a database connection

    if conn is not None:
        # create customer table
        create_table(conn, sql_create_customer_table)
    else:
        print("Unable to connect")


def create_customer(conn, customer):
    """Create a new customer for table
    :param conn:
    :param customer:
    :return: customer id
    """
    sql = ''' INSERT INTO customer(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, customer)
    return cur.lastrowid # returns the row id of the cursor object, the customer id


def select_all_customers(conn):
    """Query all rows of customer table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer")

    rows = cur.fetchall()

    return rows  # return the rows


if __name__ == '__main__':
    pass

    # delete customerDBMS.db and
    # uncomment these bottom 2 lines to rebuild customer database and table

    # conn = create_connection("customerDBMS.db")
    # create_tables(conn)
