import mysql.connector
from mysql.connector import Error

name = input("Enter Product Name: ")
desc = input("Enter Product Description: ")
price = input("Enter Product Price: ")
quantity = input("Enter Product Quantity: ")

try:
    con = mysql.connector.connect(host='localhost', database='db_products', user='root', password='')
    query = "INSERT INTO tbl_products (NAME, DESCRIPTION, PRICE, QUANTITY) VALUES ('" + name + "', '" + desc \
            + "', '" + price + "', '" + quantity + "')"
    cur = con.cursor()
    cur.execute(query)
    con.commit()
    cur.close()
    print("Successfully Inserted Record!")
except Error as error:
    print("Insert data failed {}".format(error))
finally:
    if con.is_connected():
        con.close()
        print("MySQL Connection is now CLOSED.")