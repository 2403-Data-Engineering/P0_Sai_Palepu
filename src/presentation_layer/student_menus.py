from models.student import Student
from presentation_layer.menu import Menu
from service_layer.student_service import StudentService

class NewStudentMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        New Student Menu
        """)
            
            print("First name: ")
            first_name: str = input()
            print("Last name: ")
            last_name: str = input()
            print("Major: ")
            major: str = input()
            print("Email: ")
            email: str = input()
            print("Year: ")
            year: str = input()

            new_student: Student = Student(None,first_name, last_name, major, email, year)
            print("You wanted to add this student:" + str(new_student))
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    

        new_student: Student = Student(None, first_name, last_name, major, email, year)
        self.terminal.student_service.save(new_student)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class UpdateStudentMenu(Menu):
    def render(self):
        new_dict={}
        while(True):
            print("""
        ===========================
        Update Student Menu
        """)
            print("Student ID: ")
            new_dict["student_id"] = input()
            #id: int = input()
            print("First name: ")
            new_dict["first_name"] = input()
            #first_name: str = input()
            print("Last name: ")
            #last_name: str = input()
            new_dict["last_name"] = input()
            print("Major: ")
            #major: str = input()
            new_dict["major"] = input()
            print("Email: ")
            #email: str = input()
            new_dict["email"] = input()
            print("Year: ")
            #year: str = input()
            new_dict["year"] = input()

            #new_student: Student = Student(id,first_name, last_name, major, email, year)
            print("You wanted to update the student with id : " + str(new_dict["student_id"]) + " to this information" + str(new_dict))
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    

        #new_student: Student = Student(id, first_name, last_name, major, email, year)
        self.terminal.student_service.update(new_dict)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class DeleteStudentMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        Delete Student Menu
        """)
            
            print("Student ID: ")
            id: int = input()
            print("You wanted to delete the student with this student ID:" + id +" ?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    
        self.terminal.student_service.delete_student(id)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class ViewAllStudentsMenu(Menu):
    def render(self):
        print("""
        ===========================
        View All Students
        """)
        students = self.terminal.student_service.view_all_students()
        for s in students:
            print(f"Student ID: {s['student_id']}")
            print(f"First Name: {s['first_name']}")
            print(f"Last Name: {s['last_name']}")
            print(f"Major: {s['major']}")
            print(f"Email: {s['email']}")
            print(f"Year: {s['year']}")
            print("-" * 40)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))