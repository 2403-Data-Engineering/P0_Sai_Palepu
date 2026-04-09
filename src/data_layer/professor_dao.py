from data_layer.db_connection_manager import get_connection
from models.professor import Professor

class ProfessorDao:
    def select_all_professors(self) -> list:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM professor")
            l = []
            for row in curso:
                l.append(row)
        return l

    def select_professor_by_id(self,id: int) -> Professor:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM professor WHERE professor_id = %(id)s", {"id": id})
            for row in curso:
                return Professor(**row)
        
    def select_professor_by_email(self,email: str) -> dict:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM professor WHERE email = %(email)s", {"email": email})
            for row in curso:
                return row
            
    
    def add_professor(self, pro: Professor) -> Professor:
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("INSERT INTO professor (first_name, last_name,department,email) VALUES (%(first_name)s,%(last_name)s,%(department)s,%(email)s)",
                          {"first_name":pro.first_name, "last_name":pro.last_name,"department":pro.department,"email":pro.email})
        return self.select_professor_by_email(pro.email)
    
    def delete_professor(self,id: int) -> Professor:
        deleted_professor = self.select_professor_by_id(id)
        if not deleted_professor:
            return None
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("DELETE FROM professor WHERE professor_id = %(id)s", {"id": id})
        return deleted_professor
    
    def update_professor(self,pro: Professor):
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("UPDATE professor SET first_name = %(first_name)s, last_name = %(last_name)s,department=%(department)s,email=%(email)s WHERE professor_id=%(id)s",
                          {"id":pro.professor_id,"first_name":pro.first_name, "last_name":pro.last_name,"department":pro.department,"email":pro.email})
        return self.select_professor_by_id(pro.professor_id)
    
    def ps_report(self,p_id:int):
        with get_connection() as conn:
            curso = conn.cursor(dictionary=True)
            curso.execute("SELECT * FROM professor WHERE professor_id = %(p_id)s", {"p_id": p_id})
            professor = curso.fetchone()

            if professor is None:
                    return None, None  # clean, consistent return
                    #print("That professor doesn't exist. Please try again")

            curso1 = conn.cursor(dictionary=True)
            curso1.execute("SELECT c.course_name, s.* FROM course c " \
                "INNER JOIN course_list cl on c.course_id  = cl.course_id " \
                "INNER JOIN student s on cl.student_id = s.student_id WHERE professor_id = 1",
                          {"p_id":p_id})
            from collections import defaultdict

            grouped = defaultdict(list)

            for item in curso1:
                course = item["course_name"]
    
                # Create a new dict without the "course" key
                student_data = {k: v for k, v in item.items() if k != "course_name"}
    
                grouped[course].append(student_data)

            #print(dict(grouped))
                    
            return professor,dict(grouped)