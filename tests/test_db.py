# tests/test_db.py
import os
import tempfile
from db import init_db, get_conn, DB_PATH
import students, assignments, submissions

def test_basic_flow(tmp_path, monkeypatch):
    # Put DB in tmp folder
    new_db = tmp_path / "sam.db"
    monkeypatch.setattr("db.DB_PATH", new_db)

    # Initialize DB
    init_db()

    # add student
    sid = students.add_student("Test Student", "t@example.com", "ENR001")
    assert sid > 0

    # add assignment
    aid = assignments.create_assignment("Test Assignment", "desc", None)
    assert aid > 0

    # submit
    subid = submissions.submit_assignment(sid, aid, "notes")
    assert subid > 0

    # grade
    submissions.grade_submission(subid, 85.5, "Good job")
    subs = submissions.list_submissions_for_student(sid)
    assert len(subs) == 1
    assert subs[0]['grade'] == 85.5