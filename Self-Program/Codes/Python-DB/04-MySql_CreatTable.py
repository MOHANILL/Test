import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "",
database = "SANSLevel1"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (name VARCHAR(255), address VARCHAR(255))")
print("Created")
