import mysql.connector
mydb = mysql.connector.connect(host="127.0.0.1", user="root", password = "")

# Creat Database 
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE SANSLevel1")
print("Create Database")
