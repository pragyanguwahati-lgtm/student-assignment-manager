flowchart LR
    A[User (CLI)] -->|interacts| B(main.py)
    B --> C[students.py]
    B --> D[assignments.py]
    B --> E[submissions.py]
    B --> F[analytics.py]
    C --> G[(SQLite DB)]
    D --> G
    E --> G
    F --> G

%% Use Case for SAM
actor User
User --> (Add Student)
User --> (Create Assignment)
User --> (Submit Assignment)
User --> (Grade Submission)
User --> (View Analytics)

classDiagram
    class Student {
      int id
      string name
      string email
      string enroll_no
    }
    class Assignment {
      int id
      string title
      string description
      string due_date
    }
    class Submission {
      int id
      int student_id
      int assignment_id
      string submitted_at
      float grade
    }
    Student <|-- Submission
    Assignment <|-- Submission

sequenceDiagram
    User->>main: choose "Submit assignment"
    main->>submissions: submit_assignment(student_id, assignment_id, file_path)
    submissions->>DB: INSERT submission
    DB-->>submissions: OK
    submissions-->>main: submission_id
    main->>User: display id

erDiagram
    STUDENTS {
      INTEGER id PK
      TEXT name
      TEXT email
      TEXT enroll_no
    }
    ASSIGNMENTS {
      INTEGER id PK
      TEXT title
      TEXT due_date
    }
    SUBMISSIONS {
      INTEGER id PK
      INTEGER student_id FK
      INTEGER assignment_id FK
      TEXT submitted_at
      REAL grade
    }
    STUDENTS ||--o{ SUBMISSIONS : "submits"
    ASSIGNMENTS ||--o{ SUBMISSIONS : "has"
    