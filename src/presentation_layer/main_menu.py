from presentation_layer.menu import Menu
from presentation_layer.student_menus import (NewStudentMenu, UpdateStudentMenu, DeleteStudentMenu, ViewAllStudentsMenu)
from presentation_layer.professor_menus import (NewProfessorMenu, UpdateProfessorMenu, DeleteProfessorMenu, ProfessorSummaryReportMenu, ViewAllProfessorsMenu)
from presentation_layer.course_menus import (NewCourseMenu, UpdateCourseMenu, DeleteCourseMenu, ViewAllCoursesMenu, ViewAllStudentsEnrolledInCourseMenu)
from presentation_layer.enrollment_menu import (EnrollmentMenu, StudentEnrollmentReportMenu)

class MainMenu(Menu):
    def render(self) -> None:
        print("""
    ===========================
    Welcome to uRevature Admin
    Sc) Create new student
    Su) Update Student
    Sd) Delete Student
    Pc) Create new professor
    Pu) Update professor
    Pd) Delete professor
    Cc) Create new course
    Cu) Update course
    Cd) Delete course
    E) Enroll student in course
    Ser) Student Enrollment Report
    Psr) Professor Summary Report
    Vp) View All Professors
    Vs) View All Students
    Vc) View All Courses
    Vsc) View All Students enrolled in a specific Course
    Q) Quit
            """)

        user_input: str = input().lower()
        match user_input:
            case "sc":
                print("You selected to create a new student. Please enter the necessary info")
                self.terminal.navigate(NewStudentMenu(self.terminal))
            case "su":
                print("You selected to update a student. Please enter all the information you would like to update and leave the rest blank")
                self.terminal.navigate(UpdateStudentMenu(self.terminal))
            case "sd":
                print("You selected to delete a student. Please enter the necessary info")
                self.terminal.navigate(DeleteStudentMenu(self.terminal))
            case "pc":
                print("You selected to create a new professor. Please enter the necessary info")
                self.terminal.navigate(NewProfessorMenu(self.terminal))
            case "pu":
                print("You selected to update a professor. Please enter all the information you would like to update and leave the rest blank")
                self.terminal.navigate(UpdateProfessorMenu(self.terminal))
            case "pd":
                print("You selected to delete a professor. Please enter the necessary info")
                self.terminal.navigate(DeleteProfessorMenu(self.terminal))
            case "cc":
                print("You selected to create a new course. Please enter the necessary info")
                self.terminal.navigate(NewCourseMenu(self.terminal))
            case "cu":
                print("You selected to update a course. Please enter all the information you would like to update and leave the rest blank")
                self.terminal.navigate(UpdateCourseMenu(self.terminal))
            case "cd":
                print("You selected to delete a course. Please enter the necessary info")
                self.terminal.navigate(DeleteCourseMenu(self.terminal))
            case "e":
                print("You selected to enroll a student in a course. Please enter the necessary info")
                self.terminal.navigate(EnrollmentMenu(self.terminal))
            case "ser":
                self.terminal.navigate(StudentEnrollmentReportMenu(self.terminal))
            case "psr":
                self.terminal.navigate(ProfessorSummaryReportMenu(self.terminal))
            case "vp":
                 self.terminal.navigate(ViewAllProfessorsMenu(self.terminal))
            case "vs":
                 self.terminal.navigate(ViewAllStudentsMenu(self.terminal))
            case "vc":
                 self.terminal.navigate(ViewAllCoursesMenu(self.terminal))
            case "vsc":
                 self.terminal.navigate(ViewAllStudentsEnrolledInCourseMenu(self.terminal))
            case "q":
                    self.terminal.quit()
            case _:
                    print("The option you selected does not exist. Please try again")
                    self.terminal.quit()