from __future__ import annotations
from typing import TYPE_CHECKING

from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.course_service import CourseService
from service_layer.enrollment_service import EnrollmentService


if TYPE_CHECKING:
    from presentation_layer.menu import Menu


class Terminal:
    def __init__(self, student_service: StudentService, professor_service: ProfessorService, course_service: CourseService, enrollment_service: EnrollmentService):
        from presentation_layer.main_menu import MainMenu
        self.current_menu = MainMenu(self)
        self.running = True
        self.student_service = student_service
        self.professor_service = professor_service
        self.course_service = course_service
        self.enrollment_service = enrollment_service


    def navigate(self, menu: Menu):
        
        self.current_menu = menu

    def quit(self):
        self.running = False
        print("Quitting...")