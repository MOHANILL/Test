import mysql.connector
mydb = mysql.connector.connect(
host="localhost", 
user="root", 
password = "",
database = "SANSLevel1"
)
print("Connected")
