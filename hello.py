import mysql.connector.connection

mydb= mysql.connector.connect(
    host = "localhost",
    user = "kibet",
    password= "39876700"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE  mydatabase")