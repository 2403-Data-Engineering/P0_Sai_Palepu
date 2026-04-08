from dataclasses import dataclass


@dataclass
class Course:
    course_id: int
    course_name: str
    professor_id: int