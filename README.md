# 📘 Student Assignment Manager (SAM)

A modular **Python-based CLI application** for managing students, assignments, submissions, grades, and analytics.  
Designed as a complete end-to-end project for first-year Python programming courses.

---

## 🚀 Overview

**Student Assignment Manager (SAM)** helps automate and organize the workflow of managing coursework.  
It enables:

- Adding and managing students  
- Creating and updating assignments  
- Recording submissions  
- Grading work  
- Viewing analytics  
- Exporting reports  

This project demonstrates **Python fundamentals**, modular programming, data persistence using SQLite, testing, documentation, and proper Git/GitHub usage.

---

## 🎯 Project Objectives

- Apply Python concepts in a real-world style project  
- Use modular design with clean separation of functionality  
- Implement CRUD operations  
- Store and retrieve data using SQLite  
- Implement error handling and validation  
- Practice Git & GitHub version control  
- Write complete documentation and testing scripts  

---

## 🧠 Key Features

### 👥 Student Management
- Add new students  
- View student list  
- Delete students  

### 📝 Assignment Management
- Create assignments  
- Edit/update assignments  
- List assignments  
- Delete assignments  

### 📤 Submission & Grading
- Record assignment submissions  
- Add comments and assign grades  
- View submissions per student or assignment  

### 📊 Analytics & Reporting
- Calculate **average grade** for an assignment  
- Compute **submission rate**  
- Export detailed **CSV grade reports**  

---

## 🧱 System Architecture
    User (CLI)
    │
    main.py
    ┌────────────┬────────────┬────────────┬────────────┐
    students.py assignments.py submissions.py analytics.py
    │ │ │ │
    └────────────┴────── db.py ────────────────┘
    │
    SQLite (sam.db)

---

## 📁 Folder Structure
    student-assignment-manager/
    │
    ├── main.py
    ├── db.py
    ├── students.py
    ├── assignments.py
    ├── submissions.py
    ├── analytics.py
    ├── models.py
    ├── utils.py
    │
    ├── tests/
    │ └── test_db.py
    │
    ├── data/
    │ └── sam.db (auto-created)
    │
    ├── README.md
    ├── statement.md
    ├── requirements.txt
    └── report/
    ├── report.md
    └── diagrams.md
    
---

## 🛠️ Technologies Used

- **Python 3.10+**  
- **SQLite3** (lightweight built-in database)  
- **pytest** (unit testing)  
- **ReportLab** (PDF generation for official report)  
- **VS Code**  
- **Git & GitHub**  

---

## ⚙️ Installation

### 1️⃣ Clone the repository
    git clone https://github.com/pragyanguwahati-lgtm/student-assignment-manager.git
    cd student-assignment-manager


### 2️⃣ Create and activate virtual environment
    python -m venv venv


**Windows**
    venv\Scripts\activate


**Mac/Linux**
    source venv/bin/activate


### 3️⃣ Install required packages
    pip install -r requirements.txt


### 4️⃣ Initialize the database
    python db.py

---

## ▶️ Running the Application

Run from the terminal:
    python main.py


A menu-driven interface will appear with all system functions.

---

## 🧪 Running Tests

To run unit tests:

pytest -q


---

## 🔮 Future Enhancements

- GUI interface using Tkinter/PyQt  
- Web interface using Flask/FastAPI  
- User login system (student/teacher roles)  
- File upload for assignment submissions  
- Graphical analytics dashboard  
- Email notifications for deadlines  

---

## 🧩 Learning Outcomes

Through this project, the student gains knowledge in:

- Python modular programming  
- SQLite database operations  
- CLI-based user interaction  
- Writing reusable and maintainable functions  
- Applying error handling & input validation  
- Implementing unit tests  
- Using Git/GitHub professionally  
- Creating structured project documentation  

---

## 👤 Author

Pragyanjyoti Dutta 
25BCY10065
First-Year Student at VIT-B  
Python Programming Course  (Introduction to problem solving and programming)

---

## 📚 References

- Python Documentation (docs.python.org)  
- SQLite Documentation  
- GitHub Docs  
- ReportLab Library  
- VS Code Documentation  
