import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "",
database = "SANSLevel1"
)

mycursor = mydb.cursor()
sql = " DROP TABLE customers "
mycursor.execute(sql)
print("Deleted !")
