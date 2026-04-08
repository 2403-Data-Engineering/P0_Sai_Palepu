from presentation_layer.terminal import Terminal
from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.course_service import CourseService
from service_layer.enrollment_service import EnrollmentService
from data_layer.student_dao import StudentDao
from data_layer.enrollment_dao import EnrollmentDao
from data_layer.course_dao import CourseDao
from data_layer.professor_dao import ProfessorDao

if __name__ == "__main__":
    
    terminal = Terminal(StudentService(StudentDao()), ProfessorService(ProfessorDao()), CourseService(CourseDao()), EnrollmentService(EnrollmentDao()))
    while(terminal.running):
        terminal.current_menu.render()
    print("...Goodbye!")