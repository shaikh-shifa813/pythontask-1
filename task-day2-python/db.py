import sqlite3

DB_NAME = "users.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    user_data=[
        ('ruhin','ruhin@gmail.com'),
        ('shifa','shifa@gmail.com'),
        ('aena','aena@gmail.com'),
        ('faria','faria@gmail.com')
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)",
        user_data
    )


    conn.commit()
    conn.close()

create_table()
