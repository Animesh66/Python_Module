from mysql.connector import connect

mydb = connect(host="127.0.0.1", user="root", password="nitaI9093@", database="sql_store")

my_query = """
SELECT * 
FROM customers
WHERE points BETWEEN 1000 AND 3000
ORDER BY points DESC
LIMIT 1,1;
"""

my_cursor = mydb.cursor()
my_cursor.execute(my_query)
my_result = my_cursor.fetchone()
print(my_result)
# my_results = my_cursor.fetchall()

