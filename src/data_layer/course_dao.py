from data_layer.db_connection_manager import get_connection
from models.course import Course
class CourseDao:
    def select_all_courses(self) -> list:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM course")
            l = []
            for row in curso:
                l.append(row)
        return l

    def select_course_by_id(self,id: int) -> Course:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM course WHERE course_id = %(id)s", {"id": id})
            for row in curso:
                return Course(**row)
        
    
    def add_course(self, cou: Course) -> Course:
        
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("INSERT INTO course (course_name, professor_id) VALUES (%(course_name)s,%(professor_id)s)",
                {"course_name":cou.course_name, "professor_id":cou.professor_id,})
        return self.select_course_by_id(cou.course_id)
    
    def delete_course(self,id: int) -> Course:
        deleted_course = self.select_course_by_id(id)
        if not deleted_course:
            return None
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("DELETE FROM course WHERE course_id = %(id)s", {"id": id})
        return deleted_course
    
    def update_course(self,cou: Course):
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("UPDATE course SET course_name = %(course_name)s, professor_id = %(professor_id)s WHERE course_id = %(course_id)s",
                          {"course_id":cou.course_id,"course_name":cou.course_name, "professor_id":cou.professor_id})
        return self.select_course_by_id(cou.course_id)
    
    def select_all_students_enrolled_in_course(self,c_id:int):
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM course WHERE course_id = %(id)s", {"id": c_id})
            course = curso.fetchone()
            if course is None:
                print("That course doesn't exist. Please try again")
                return None, None
            curso1 = conn.cursor(dictionary=True, buffered=True)
            curso1.execute("SELECT student_id FROM course_list WHERE course_id = %(id)s", {"id": c_id})
            curso2 = conn.cursor(dictionary=True, buffered=True)
            curso2.execute("SELECT * FROM student")
            l=[]
            for c1 in curso1:
                for c2 in curso2:
                    if c1["student_id"]==c2["student_id"]:
                        l.append(c2)
        return course,l