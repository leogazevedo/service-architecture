import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "/data/tasks.db")


def get_connection() -> sqlite3.Connection:
    # use of sqlite which is Python native.
    conn = sqlite3.connect(DB_PATH)
    # Configure sqlite to allow access its data by column name 
    # (i.e., row["column"]) instead of by index.
    conn.row_factory = sqlite3.Row 
    return conn


def init_db():
    # create the table it does not exist.
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS task (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       TEXT    NOT NULL,
                description TEXT,
                done        INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.commit()



