from data_layer.db_connection_manager import get_connection
from models.student import Student

class StudentDao:
    def select_all_students(self) -> list:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM student")
            l = []
            for row in curso:
                l.append(row)
        return l

    def select_student_by_id(self,id: int) -> Student:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM student WHERE student_id = %(id)s", {"id": id})
            for row in curso:
                return Student(**row)
        
    def select_student_by_email(self,email: str) -> dict:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM student WHERE email = %(email)s", {"email": email})
            for row in curso:
                return row
            
    
    def add_student(self, stu: Student) -> Student:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("INSERT INTO student (first_name, last_name,major,email,year) VALUES (%(first_name)s,%(last_name)s,%(major)s,%(email)s,%(year)s)",
                          {"first_name":stu.first_name, "last_name":stu.last_name,"major":stu.major,"email":stu.email,"year":stu.year})
        return self.select_student_by_email(stu.email)
    
    def delete_student(self,id: int) -> Student:
        deleted_student = self.select_student_by_id(id)
        if not deleted_student:
            return None
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("DELETE FROM student WHERE student_id = %(id)s", {"id": id})
        return deleted_student
    
    def update_student(self,stu: Student):
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("UPDATE student SET first_name = %(first_name)s, last_name = %(last_name)s,major=%(major)s,email=%(email)s,year =%(year)s WHERE student_id=%(id)s",
                          {"id":stu.student_id,"first_name":stu.first_name, "last_name":stu.last_name,"major":stu.major,"email":stu.email,"year":stu.year})
        return self.select_student_by_email(stu.email)
            

