from mysql.connector import connect

mydb = connect(host="",user="",password="",database="")

my_cursor = mydb.cursor()
my_cursor.execute("write MySql query")
my_result= my_cursor.fetchone()