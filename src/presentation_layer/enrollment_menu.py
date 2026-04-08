

from presentation_layer.menu import Menu


class EnrollmentMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        Enrollment Menu
        """)
            
            print("Course ID: ")
            c_id: int = input()
            print("Student ID: ")
            s_id: int = input()

            print("You wanted to add student with id: " + str(s_id) + " to course with id: " + str(c_id) + " ?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
        self.terminal.enrollment_service.enroll(c_id, s_id)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class StudentEnrollmentReportMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        Enrollment Menu
        """)
            
            print("Student ID: ")
            s_id: int = input()

            print("You wanted to view all courses enrolled in by the student with id: " + str(s_id) + "?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
        student, l = self.terminal.enrollment_service.enrollment_report(s_id)
        from mdutils.mdutils import MdUtils

        # Initialize the file
        md_file = MdUtils(file_name='student_enrollment_report', title=('Student Enrollment Report for student_id: '+str(student["student_id"])))

        # Add headers and paragraphs
        md_file.new_header(level=1, title='Student Information')
        md_file.new_paragraph(f"""
        Student ID: {student['student_id']}  
        First Name: {student['first_name']} 
        Last Name: {student['last_name']}  
        Email: {student['email']}  
        Year:{student['year']}
        """)

        # Create a list
        md_file.new_header(level=2, title="Courses")
        table_data = ["Course ID", "Course Name"]

        for c in l:
            table_data.extend([
                str(c['course_id']),
                c['course_name']
            ])

        md_file.new_table(
            columns=2,
            rows=len(l) + 1,
            text=table_data
        )
        #l2 = []

        #for item in l:
            #l2.append(str(item))
        #md_file.new_list(l2)

        # Finalize and save
        md_file.create_md_file()
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))
            