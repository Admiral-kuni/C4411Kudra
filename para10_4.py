import sqlite3

connection = sqlite3.connect("ITStep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
connection.close()
res = cur.fetchall()
print(res)
connection.close()