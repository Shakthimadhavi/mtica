import sqlite3 as lite
con = lite.connect('mtica.db')

cur = con.cursor()
cur.execute("Drop TABLE IF EXISTS Cars")
cur.execute(''' CREATE TABLE Cars(
         ID INT, Name TEXT, Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
cur.execute("INSERT INTO Cars VALUES(3,'skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(4,'volvo',29000)")
cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
cur.execute("INSERT INTO Cars VALUES(6,'citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(7,'hummer',41400)")
cur.execute("INSERT INTO Cars VALUES(8,'volkswagen',21600)")
con.commit()
print("values in table car inserted.")
