from data_layer.enrollment_dao import EnrollmentDao
import mysql.connector
from mysql.connector import errorcode
class EnrollmentService:
    def __init__(self, e_dao: EnrollmentDao):
        self.e_dao = e_dao
    def enroll(self, c_id:int, s_id:int):
        try:
            self.e_dao.enroll_student(c_id, s_id)
        except:
            print("That student is already enrolled in that course")
    def enrollment_report(self,s_id):
        student, l = self.e_dao.enrollment_report_list(s_id)
        return student, l