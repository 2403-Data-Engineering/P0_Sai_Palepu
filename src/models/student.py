from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    first_name: str
    last_name: str
    major: str
    email: str
    year: str