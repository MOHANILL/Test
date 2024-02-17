import sqlite3

conn = sqlite3.connect('my_database.db')

c =conn.cursor()

c.execute(' DELETE FROM customers WHERE name = "Mobin" ')

conn.commit()
print(c.rowcount, "record(s) deleted!")
conn.close()