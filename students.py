# students.py
from db import get_conn
from models import Student

def add_student(name: str, email: str = None, enroll_no: str = None):
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO students (name, email, enroll_no, created_at) VALUES (?, ?, ?, datetime('now'))",
            (name, email, enroll_no)
        )
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()

def list_students():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY name")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_student(student_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def delete_student(student_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()