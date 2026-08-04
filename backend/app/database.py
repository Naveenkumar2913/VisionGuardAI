import sqlite3

DATABASE_NAME = "visionguard.db"

def connect_db():
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        track_id INTEGER,
        zone TEXT,
        event_time TEXT,
        screenshot TEXT
    )
    """)

    conn.commit()
    conn.close()

print("Database initialized.")