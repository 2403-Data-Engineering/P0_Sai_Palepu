from models.professor import Professor
from data_layer.professor_dao import ProfessorDao
import mysql.connector
from mysql.connector import errorcode
class ProfessorService:
    def __init__(self, p_dao: ProfessorDao):
        self.p_dao = p_dao
    def save(self, professor: Professor) -> Professor:
        try:
            for key, value in professor.__dict__.items():
                if not value:
                    setattr(professor, key, None)
            new_professor= self.p_dao.add_professor(professor)
            return new_professor
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("Duplicate email detected. Please enter in a unique email.")

            elif err.errno == errorcode.ER_BAD_NULL_ERROR:
                print("A required field is missing.")

            else:
                print(f"Database error: {err}")
        return None
    def update(self, new_dict: dict) -> None:
        old_professor = self.p_dao.select_professor_by_id(new_dict["professor_id"])
        if not old_professor:
            print("That professor doesn't exist. Please try again")
            return None
        for k, v in new_dict.items():
            if not v:
                new_dict[k] = getattr(old_professor,k)
        try:
            updated_professor = self.p_dao.update_professor(Professor(**new_dict))
            print("Professor UPDATED!")
            print("Updated professor: " + str(updated_professor))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                print("Duplicate email detected. Please enter in a unique email.")
            else:
                print(f"Database error: {err}")
        
    def delete(self, id:int):
        p = self.p_dao.delete_professor(id)
        if not p:
            print("That professor doesn't exist in the database")
        else:
            print("Deleted this professor: " + str(p))
    def ps_report(self,p_id:int):
        professor, ce_dict = self.p_dao.ps_report(p_id)
        return professor, ce_dict
    def view_all_profs(self):
        l = self.p_dao.select_all_professors()
        return l