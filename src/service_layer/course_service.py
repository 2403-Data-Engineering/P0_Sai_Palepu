from data_layer.course_dao import CourseDao
from models.course import Course
import mysql.connector
from mysql.connector import errorcode

class CourseService:
    def __init__(self, c_dao: CourseDao):
        self.c_dao = c_dao

    def save(self, course: Course) -> Course:
        try:
            new_course = self.c_dao.add_course(course)
            return new_course
        except mysql.connector.IntegrityError as err:
            print("Please enter a valid professor id")
            return None
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
                

    def update(self, new_dict: dict) -> None:
        old_course = self.c_dao.select_course_by_id(new_dict["course_id"])
        for k, v in new_dict.items():
            if not v:
                new_dict[k] = getattr(old_course,k)
        try:
            updated_course = self.c_dao.update_course(Course(**new_dict))
            print("Course UPDATED!")
            print("Updated course: " + str(updated_course))
        except mysql.connector.IntegrityError as err:
            print("Please enter a valid professor id")
            return None
        except mysql.connector.Error as err:
            print(f"Database error: {err}")

    def delete(self, id:int):
        c = self.c_dao.select_course_by_id(id)
        if not c:
            print("That course doesn't exist in the database. Please try again")
        else:
            print("Deleted this course: " + str(c))

    def view_all_courses(self):
        l = self.c_dao.select_all_courses()
        return l

    def vasec(self, course_id:int):
        course,l = self.c_dao.select_all_students_enrolled_in_course(course_id)
        return course,l