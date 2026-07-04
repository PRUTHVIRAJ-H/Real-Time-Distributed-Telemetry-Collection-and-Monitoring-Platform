import sqlite3

DB_NAME = "telemetry.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS devices(
            device_id TEXT PRIMARY KEY,
            ip TEXT,
            first_seen TEXT,
            last_seen TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS telemetry(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            value REAL,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()