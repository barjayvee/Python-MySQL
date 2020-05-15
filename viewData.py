import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost', database='db_products', username='root', password='')
    query = "SELECT * FROM tbl_products"
    cur = con.cursor()
    cur.execute(query)
    records = cur.fetchall()
    print("Number of records in the table: ", cur.rowcount)
    for row in records:
        print("ID : ", row[0])
        print("NAME : ", row[1])
        print("DESCRIPTION : ", row[2])
        print("PRICE : ", row[3])
        print("QUANTITY : ", row[4])
        print("----------------------")
except Error as error:
    print("Error in the program {}".format(error))
finally:
    if con.is_connected():
        cur.close()
        con.close()
        print("MySQL Connection is now CLOSED!")