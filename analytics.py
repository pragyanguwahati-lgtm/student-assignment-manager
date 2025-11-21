# analytics.py
import csv
from db import get_conn

def average_grade_by_assignment(assignment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT AVG(grade) as avg_grade FROM submissions WHERE assignment_id=? AND grade IS NOT NULL", (assignment_id,))
    row = cur.fetchone()
    conn.close()
    return row['avg_grade'] if row else None

def submission_rate(assignment_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) as total_subs FROM submissions WHERE assignment_id=?", (assignment_id,))
    total_subs = cur.fetchone()['total_subs']
    cur.execute("SELECT COUNT(*) as total_students FROM students")
    total_students = cur.fetchone()['total_students']
    conn.close()
    if total_students == 0:
        return 0.0
    return total_subs / total_students

def export_assignment_report_csv(assignment_id, out_path):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
    SELECT s.id as submission_id, st.name as student_name, st.enroll_no, s.submitted_at, s.file_path, s.grade, s.comments
    FROM submissions s
    JOIN students st ON s.student_id = st.id
    WHERE s.assignment_id = ?
    """, (assignment_id,))
    rows = cur.fetchall()
    conn.close()
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["submission_id", "student_name", "enroll_no", "submitted_at", "file_path", "grade", "comments"])
        for r in rows:
            writer.writerow([r['submission_id'], r['student_name'], r['enroll_no'], r['submitted_at'], r['file_path'], r['grade'], r['comments']])
    return out_path