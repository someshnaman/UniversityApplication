from dbqueries import Dbqueries
from cassandradatabase import Database
import logger
import constants

logs = logger.Logs()


class Course:
    def __init__(self):
        self.course_id = None
        self.course_code = None
        self.courseName = None
        self.courseDesc = None
        self.courseImageUrl = None
        self.courseDuration = None
        # self.createdOn = None  # Datatype would be Timestamp
        # self.modifiedOn = None  # Datatype would be Timestamp

    def insertCourse(self, value):
        try:
            dbobject = Database()
            return dbobject.insert(constants.query_insert_course, value)
        except Exception as e:
            logs.exception(e)

    def findAllCourses(self):
        try:
            dbobject = Database()
            result = dbobject.findAll("course1")
            return result
        except Exception as e:
            logs.exception(e)


somesh = Course()
result = somesh.findAllCourses()
