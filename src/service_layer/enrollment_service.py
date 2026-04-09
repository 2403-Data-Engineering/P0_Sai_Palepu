from data_layer.enrollment_dao import EnrollmentDao
import mysql.connector
from mysql.connector import errorcode
class EnrollmentService:
    def __init__(self, e_dao: EnrollmentDao):
        self.e_dao = e_dao
    def enroll(self, c_id:int, s_id:int):
        try:
            self.e_dao.enroll_student(c_id, s_id)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("That student is already enrolled in that course")
    def enrollment_report(self,s_id):
        try:
            student, l = self.e_dao.enrollment_report_list(s_id)
            if student is None:
                return None, None
            
            return student, l
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return None, None