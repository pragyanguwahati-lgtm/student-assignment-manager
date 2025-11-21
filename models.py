# models.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Student:
    id: Optional[int]
    name: str
    email: Optional[str]
    enroll_no: Optional[str]
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()

@dataclass
class Assignment:
    id: Optional[int]
    title: str
    description: Optional[str]
    due_date: Optional[str]
    created_at: str = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()

@dataclass
class Submission:
    id: Optional[int]
    student_id: int
    assignment_id: int
    submitted_at: str = None
    file_path: Optional[str] = None
    grade: Optional[float] = None
    comments: Optional[str] = None

    def __post_init__(self):
        if self.submitted_at is None:
            self.submitted_at = datetime.utcnow().isoformat()