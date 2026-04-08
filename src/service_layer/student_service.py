from models.student import Student
from data_layer.student_dao import StudentDao
import mysql.connector
from mysql.connector import errorcode

class StudentService:
    def __init__(self, s_dao: StudentDao):
        self.s_dao = s_dao

    def save(self, student: Student) -> Student:
        try:
            for key, value in student.__dict__.items():
                if not value:
                    setattr(student, key, None)
            new_student = self.s_dao.add_student(student)
            return new_student
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("Duplicate email detected. Please enter in a unique email.")

            elif err.errno == errorcode.ER_BAD_NULL_ERROR:
                print("A required field is missing.")

            else:
                print(f"Database error: {err}")

        return None
        #except:
            #print("All emails are unique. You entered in a duplicate email. Please try again.")
            #return None
        
    def update(self, new_dict: dict) -> None:
        old_student = self.s_dao.select_student_by_id(new_dict["student_id"])
        if not old_student:
            print("That student doesn't exist. Please try again")
            return None
        for k, v in new_dict.items():
            if not v:
                new_dict[k] = old_student[k]
        updated_student = self.s_dao.update_student(Student(**new_dict))
        print("STUDENT UPDATED!")
        print(updated_student)

    def view_all_students(self):
        l = self.s_dao.select_all_students()
        return l

    def get_student_by_id(self, id:int):
        print(self.s_dao.select_student_by_id(id))
        
    def delete_student(self, id:int):
        s = self.s_dao.delete_student(id)
        if not s:
            print("That student doesn't exist in the database")
        else:
            print("Deleted this student: " + str(s))