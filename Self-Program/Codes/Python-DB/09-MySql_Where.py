import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "",
database = "SANSLevel1"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address='PARK lANE 38' "
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:
    print(x)
