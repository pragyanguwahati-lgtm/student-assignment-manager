# submissions.py
from db import get_conn
from datetime import datetime

def submit_assignment(student_id, assignment_id, file_path=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO submissions (student_id, assignment_id, submitted_at, file_path)
    VALUES (?, ?, datetime('now'), ?)
    """, (student_id, assignment_id, file_path))
    conn.commit()
    last = cur.lastrowid
    conn.close()
    return last

def grade_submission(submission_id, grade, comments=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE submissions SET grade=?, comments=? WHERE id=?", (grade, comments, submission_id))
    conn.commit()
    conn.close()

def list_submissions_for_assignment(assignment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT s.*, st.name as student_name FROM submissions s JOIN students st ON s.student_id=st.id WHERE s.assignment_id=?",
                (assignment_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def list_submissions_for_student(student_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT s.*, a.title as assignment_title FROM submissions s JOIN assignments a ON s.assignment_id=a.id WHERE s.student_id=?",
                (student_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]