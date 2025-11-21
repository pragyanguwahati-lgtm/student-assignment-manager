# assignments.py
from db import get_conn
from models import Assignment

def create_assignment(title, description=None, due_date=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO assignments (title, description, due_date, created_at) VALUES (?, ?, ?, datetime('now'))",
                (title, description, due_date))
    conn.commit()
    last = cur.lastrowid
    conn.close()
    return last

def list_assignments():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM assignments ORDER BY due_date")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_assignment(assignment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM assignments WHERE id = ?", (assignment_id,))
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def update_assignment(assignment_id, title=None, description=None, due_date=None):
    a = get_assignment(assignment_id)
    if not a:
        return False
    title = title or a['title']
    description = description if description is not None else a['description']
    due_date = due_date or a['due_date']
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE assignments SET title=?, description=?, due_date=? WHERE id=?",
                (title, description, due_date, assignment_id))
    conn.commit()
    conn.close()
    return True

def delete_assignment(assignment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM assignments WHERE id = ?", (assignment_id,))
    conn.commit()
    conn.close()