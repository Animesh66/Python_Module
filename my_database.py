from mysql.connector import connect
import os

db_password = os.getenv("DB_PASSWORD")
mydb = connect(host="127.0.0.1", user="root", password=db_password, database="sql_store")

my_query = """
SELECT * 
FROM customers
WHERE points BETWEEN 1000 AND 3000
ORDER BY points DESC
LIMIT 1,1;
"""
my_new_query = """
SELECT * 
FROM customers
WHERE points BETWEEN 1000 AND 3000
ORDER BY points DESC;
"""

my_cursor = mydb.cursor()
my_cursor.execute(my_query)
my_result = my_cursor.fetchone()
print(my_result)
my_cursor.execute(my_new_query)
my_new_result = my_cursor.fetchall()
print(my_new_result)
print(my_new_result[1][4])


