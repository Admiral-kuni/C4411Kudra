import sqlite3
connection = sqlite3.connect("ITStep_DB.sl3", 5)
cur = connection.cursor()
print(connection)
print(cur)
connection.close()