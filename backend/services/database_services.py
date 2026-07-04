from datetime import datetime
from database.db import get_connection


def save_device(node):
    conn = get_connection()

    conn.execute("""
        INSERT OR REPLACE INTO devices
        VALUES (?, ?, ?, ?)
    """, (
        node["device_id"],
        node["ip"],
        node["first_seen"].isoformat(),
        node["last_seen"].isoformat()
    ))

    conn.commit()
    conn.close()


def save_telemetry(device_id, value):
    conn = get_connection()

    conn.execute("""
        INSERT INTO telemetry(
            device_id,
            value,
            timestamp
        )
        VALUES (?, ?, ?)
    """, (
        device_id,
        value,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()