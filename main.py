# main.py
import sys
from db import init_db
import students, assignments, submissions, analytics
from utils import parse_date, pretty_row

def main_menu():
    print("\nStudent Assignment Manager (SAM)")
    print("1) Students")
    print("2) Assignments")
    print("3) Submissions")
    print("4) Analytics & Reports")
    print("0) Exit")
    return input("Choose: ").strip()

def students_menu():
    while True:
        print("\nSTUDENTS MENU")
        print("1) Add student")
        print("2) List students")
        print("3) Delete student")
        print("0) Back")
        c = input("Choose: ").strip()
        if c == "1":
            name = input("Name: ")
            email = input("Email (optional): ") or None
            enroll = input("Enroll No (optional): ") or None
            try:
                sid = students.add_student(name, email, enroll)
                print("Added student id", sid)
            except Exception as e:
                print("Error:", e)
        elif c == "2":
            for s in students.list_students():
                print(pretty_row(s))
        elif c == "3":
            sid = input("Student ID to delete: ")
            students.delete_student(int(sid))
            print("Deleted (if existed).")
        elif c == "0":
            return
        else:
            print("Invalid")

def assignments_menu():
    while True:
        print("\nASSIGNMENTS MENU")
        print("1) Create assignment")
        print("2) List assignments")
        print("3) Update assignment")
        print("4) Delete assignment")
        print("0) Back")
        c = input("Choose: ").strip()
        if c == "1":
            title = input("Title: ")
            desc = input("Description (optional): ") or None
            due = input("Due date (YYYY-MM-DD, optional): ") or None
            try:
                due_iso = parse_date(due) if due else None
            except Exception as e:
                print("Bad date:", e)
                continue
            aid = assignments.create_assignment(title, desc, due_iso)
            print("Created assignment id", aid)
        elif c == "2":
            for a in assignments.list_assignments():
                print(pretty_row(a))
        elif c == "3":
            aid = int(input("Assignment ID to update: "))
            title = input("New title (leave blank to keep): ") or None
            desc = input("New desc (leave blank to keep): ") or None
            due = input("New due date (optional): ") or None
            try:
                due_iso = parse_date(due) if due else None
            except Exception as e:
                print("Bad date:", e)
                continue
            ok = assignments.update_assignment(aid, title, desc, due_iso)
            print("Updated:", ok)
        elif c == "4":
            aid = int(input("Assignment ID to delete: "))
            assignments.delete_assignment(aid)
            print("Deleted (if existed)")
        elif c == "0":
            return
        else:
            print("Invalid option")

def submissions_menu():
    while True:
        print("\nSUBMISSIONS MENU")
        print("1) Submit assignment (record)")
        print("2) Grade submission")
        print("3) List submissions for assignment")
        print("4) List submissions for student")
        print("0) Back")
        c = input("Choose: ").strip()
        if c == "1":
            sid = int(input("Student ID: "))
            aid = int(input("Assignment ID: "))
            fpath = input("File path / notes (optional): ") or None
            subid = submissions.submit_assignment(sid, aid, fpath)
            print("Recorded submission id", subid)
        elif c == "2":
            subid = int(input("Submission ID: "))
            grade = float(input("Grade (0-100): "))
            comments = input("Comments (optional): ") or None
            submissions.grade_submission(subid, grade, comments)
            print("Graded.")
        elif c == "3":
            aid = int(input("Assignment ID: "))
            for r in submissions.list_submissions_for_assignment(aid):
                print(pretty_row(r))
        elif c == "4":
            sid = int(input("Student ID: "))
            for r in submissions.list_submissions_for_student(sid):
                print(pretty_row(r))
        elif c == "0":
            return
        else:
            print("Invalid.")

def analytics_menu():
    while True:
        print("\nANALYTICS & REPORTS")
        print("1) Average grade for assignment")
        print("2) Submission rate for assignment")
        print("3) Export assignment report to CSV")
        print("0) Back")
        c = input("Choose: ").strip()
        if c == "1":
            aid = int(input("Assignment ID: "))
            avg = analytics.average_grade_by_assignment(aid)
            print("Average grade:", avg)
        elif c == "2":
            aid = int(input("Assignment ID: "))
            rate = analytics.submission_rate(aid)
            print(f"Submission rate: {rate:.2%}")
        elif c == "3":
            aid = int(input("Assignment ID: "))
            out = input("Output CSV path (e.g. report_assignment1.csv): ")
            path = analytics.export_assignment_report_csv(aid, out)
            print("Exported to", path)
        elif c == "0":
            return
        else:
            print("Invalid")

def main():
    init_db()
    while True:
        c = main_menu()
        if c == "1":
            students_menu()
        elif c == "2":
            assignments_menu()
        elif c == "3":
            submissions_menu()
        elif c == "4":
            analytics_menu()
        elif c == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()