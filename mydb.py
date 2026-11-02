import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4768",
)

mycursor = database.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS crm")

print("Database created successfully")