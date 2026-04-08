from data_layer.db_connection_manager import get_connection
from models.student import Student
from models.course import Course
class EnrollmentDao:
    def enroll_student(self, c_id:int, s_id:int):
            with get_connection() as conn:
                curso = conn.cursor(dictionary=True)

                curso.execute("INSERT INTO course_list (course_id, student_id) VALUES (%(course_id)s,%(student_id)s)",
                            {"course_id":c_id, "student_id":s_id})
        
    def enrollment_report_list(self,s_id:int):
        with get_connection() as conn:
            l = []
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM student WHERE student_id = %(student_id)s", {"student_id": s_id})
            for row in curso:
                student = row
                if not student:
                    print("That student doesn't exist. Please try again")
                    return None
            curso1 = conn.cursor(dictionary=True, buffered=True)
            curso1.execute("SELECT * FROM course_list WHERE student_id = %(student_id)s",
                          {"student_id":s_id})
            curso2 = conn.cursor(dictionary=True,buffered=True)
            curso2.execute("SELECT * from course")
            for c1 in curso1:
                for c2 in curso2:
                    if c1["course_id"]==c2["course_id"]:
                        l.append(c2)
                    
            return student,l



