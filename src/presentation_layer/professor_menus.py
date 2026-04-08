from models.professor import Professor
from presentation_layer.menu import Menu
from service_layer.professor_service import ProfessorService

class NewProfessorMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        New Professor Menu
        """)
            
            print("First name: ")
            first_name: str = input()
            print("Last name: ")
            last_name: str = input()
            print("Department: ")
            department: str = input()
            print("Email: ")
            email: str = input()

            new_professor: Professor = Professor(None,first_name, last_name, department, email)
            print("You wanted to add this professor:" + str(new_professor))
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    

        new_professor: Professor = Professor(None, first_name, last_name, department, email)
        self.terminal.professor_service.save(new_professor)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class UpdateProfessorMenu(Menu):
    def render(self):
        new_dict={}
        while(True):
            print("""
        ===========================
        Update Professor Menu
        """)
            
            print("Professor ID:")
            new_dict["professor_id"]=input()
            #id:int = input()
            print("First name: ")
            new_dict["first_name"]=input()
            #first_name: str = input()
            print("Last name: ")
            #last_name: str = input()
            new_dict["last_name"]=input()
            print("Department: ")
            new_dict["department"]=input()
            #department: str = input()
            print("Email: ")
            new_dict["email"]=input()
            #email: str = input()

            #new_professor: Professor = Professor(id,first_name, last_name, department, email)
            print("You wanted to update the professor with id: " + str(new_dict["professor_id"]) + " to this info " + str(new_dict) + "?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    

        #new_professor: Professor = Professor(id, first_name, last_name, department, email)
        self.terminal.professor_service.update(new_dict)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class DeleteProfessorMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        Delete Professor Menu
        """)
            
            print("Professor ID: ")
            id: int = input()
            print("You wanted to delete the professor with this professor ID:" + id +" ?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    
        self.terminal.professor_service.delete(id)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class ViewAllProfessorsMenu(Menu):
    def render(self):
        print("""
        ===========================
        View All Professors
        """)
        professors = self.terminal.professor_service.view_all_profs()
        for p in professors:
            print(f"Professor ID: {p['professor_id']}")
            print(f"First Name: {p['first_name']}")
            print(f"Last Name: {p['last_name']}")
            print(f"Department: {p['department']}")
            print(f"Email: {p['email']}")
            print("-" * 40)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class ProfessorSummaryReportMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        Professor Summary Report Menu
        """)
            
            print("Professor ID: ")
            p_id: int = input()

            print("You wanted to view the summary for the professor with id: " + str(p_id) + "?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
        prof, c_dict = self.terminal.professor_service.ps_report(p_id)
        from mdutils.mdutils import MdUtils

        # Initialize the file
        md_file = MdUtils(file_name='professor_summary_report', title=('Professor Summary Report for professor_id: '+str(prof["professor_id"])))

        # Add headers and paragraphs
        md_file.new_header(level=1, title='Professor Information')
        md_file.new_paragraph(f"""
        Professor ID: {prof['professor_id']}  
        First Name: {prof['first_name']} 
        Last Name: {prof['last_name']}  
        Email: {prof['email']}  
        Department: {prof['department']}
        """)
        md_file.new_header(level=2, title="Courses")

        for course, students in c_dict.items():
            # Course name as sub-header
            md_file.new_header(level=3, title=course)

            table_data = ["Student ID", "First Name", "Last Name", "Major", "Email", "Year"]

            for s in students:
                table_data.extend([
                    str(s['student_id']),
                    s['first_name'],
                    s['last_name'],
                    s['major'],
                    s['email'],
                    str(s['year'])
                ])

            md_file.new_table(
                columns=6,
                rows=len(students) + 1,
                text=table_data
            )

            md_file.new_line()
        md_file.create_md_file()
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))
