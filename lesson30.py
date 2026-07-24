import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")

rows = cursor.fetchall()

for row in rows:
    print("Username:", row[0])
    print("Password:", row[1])
    print("----------------")

conn.close()
