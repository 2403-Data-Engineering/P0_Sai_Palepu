
from models.course import Course
from presentation_layer.menu import Menu


class NewCourseMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        New Course Menu
        """)
            
            print("Course name: ")
            course_name: str = input()
            print("Professor ID: ")
            p_id: int = input()

            new_course: Course = Course(None,course_name, p_id)
            print("You wanted to add this course: " + str(new_course))
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    

        new_class: Course = Course(None, course_name, p_id)
        self.terminal.course_service.save(new_class)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class UpdateCourseMenu(Menu):
    def render(self):
        new_dict={}
        while(True):
            print("""
        ===========================
        Update Course Menu
        """)
            
            print("Course ID: ")
            new_dict["course_id"] = input()
            #course_id: int = input()
            print("Course name: ")
            #course_name: str = input()
            new_dict["course_name"] = input()
            print("Professor ID: ")
            #p_id: int = input()
            new_dict["professor_id"] = input()

            #new_course: Course = Course(course_id,course_name, p_id)
            print("You wanted to update the course with id : " + str(new_dict["course_id"]) + " to this information" + str(new_dict))
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    
        #new_course: Course = Course(course_id, course_name, p_id)
        self.terminal.course_service.update(new_dict)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class DeleteCourseMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        Delete Course Menu
        """)
            
            print("Course ID: ")
            id: int = input()
            print("You wanted to delete the course with this course ID:" + id +" ?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    
        self.terminal.course_service.delete(id)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class ViewAllCoursesMenu(Menu):
    def render(self):
        print("""
        ===========================
        View All Courses
        """)
        courses = self.terminal.course_service.view_all_courses()
        for course in courses:
            print(f"Course ID: {course['course_id']}")
            print(f"Course Name: {course['course_name']}")
            print(f"Professor ID: {course['professor_id']}")
            print("-" * 40)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))

class ViewAllStudentsEnrolledInCourseMenu(Menu):
    def render(self):
        while(True):
            print("""
        ===========================
        View All Students enrolled in a specific Course Menu
        """)
            
            print("Course ID: ")
            id: int = input()
            print("You wanted to view all the students enrolled in the course with this course ID:" + id +" ?")
            print("Is this correct? Y or N?")
            user_input: str = input().lower()
            match user_input:
                case "y":
                    break;
                case "n":
                    print("Please re-enter the information")
                    
        course, students = self.terminal.course_service.vasec(id)
        if course is None:
            print("❌ Course not found. Please try again.")
            return
        print()
        print("Course Name: " + str(course["course_name"]))
        print("-" * 40)
        print("Students Enrolled:")
        print()
        for s in students:
            print(f"Student ID: {s['student_id']}")
            print(f"First Name: {s['first_name']}")
            print(f"Last Name: {s['last_name']}")
            print(f"Major: {s['major']}")
            print(f"Email: {s['email']}")
            print(f"Year: {s['year']}")
            print("-" * 30)
        from presentation_layer.main_menu import MainMenu
        self.terminal.navigate(MainMenu(self.terminal))