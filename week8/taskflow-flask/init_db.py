import sqlite3

conn = sqlite3.connect("tasks.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT
)
""")

conn.commit()
conn.close()

print("Database created!")
