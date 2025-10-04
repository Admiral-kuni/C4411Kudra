import sqlite3

connection = sqlite3.connect("ITStep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Nick')")
cur.execute(" INSERT INTO first_table (name) VALUES ('Vasya')")
connection.commit()
connection.close()
