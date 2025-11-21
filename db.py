# db.py
import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("data") / "sam.db"

def get_conn():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE,
        enroll_no TEXT UNIQUE,
        created_at TEXT NOT NULL
    );""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        created_at TEXT NOT NULL
    );""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS submissions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        assignment_id INTEGER NOT NULL,
        submitted_at TEXT NOT NULL,
        file_path TEXT,
        grade REAL,
        comments TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(assignment_id) REFERENCES assignments(id)
    );""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized at", DB_PATH)