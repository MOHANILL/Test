import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "",
database = "SANSLevel1"
)

mycursor = mydb.cursor()
sql = " DROP database sanslevel1 "
mycursor.execute(sql)
print("Deleted !")
