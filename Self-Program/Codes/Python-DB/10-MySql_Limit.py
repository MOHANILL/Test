import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "",
database = "SANSLevel1"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 3")
myresult = mycursor.fetchall()


for x in myresult:
    print(x)
