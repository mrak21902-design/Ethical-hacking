import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

cursor.execute(
    "INSERT INTO users VALUES (?, ?)",
    ("Rani", "Ranil@123")
)

conn.commit()

print("User Saved Successfully!")

conn.close()
