from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired

import database.constants as constants
from database.cassandradatabase import Database
from database.logger import Logs

logs = Logs()


class Course():

    def __init__(self):
        self.course_id = None
        self.course_code = None
        self.course_name = None
        self.course_desc = None
        self.course_imageUrl = None
        self.course_duration = None
        # self.createdOn = None  # Datatype would be Timestamp
        # self.modifiedOn = None  # Datatype would be Timestamp

    def __init__(self, course_id, course_code, course_desc, course_name, course_duration, course_imageUrl):
        self.course_id = course_id
        self.course_code = course_code
        self.course_name = course_name
        self.course_desc = course_desc
        self.course_imageUrl = course_imageUrl
        self.course_duration = course_duration


class CourseDao:  # Data access Object
    def insertCourse(self, value):
        try:
            """
            This function is used for inserting course into the database.
            the Data type of Value attribute here is List or tuple where 6 element
            will be there. 
            """
            db_object = Database()
            insert_result = db_object.insert(constants.query_insert_course, value)
            return insert_result
        except Exception as e:
            logs.exception(e)

    def findCourseById(self, course_id):
        try:
            db_object = Database()
            result = db_object.session.execute(f"select * from course1 where courseID={course_id}")
            course_object = Course(result[0].courseid, result[0].coursecode,
                                   result[0].coursedesc, result[0].coursename,
                                   result[0].courseduration, result[0].courseimageurl)
            return course_object
        except Exception as e:
            logs.exception(e)

    def findAllCourses(self):
        try:
            db_object = Database()
            course_result = db_object.findAll("course1")
            course_list = []
            for i in course_result:
                course_list.append(self.convertToCourse(i))
            return course_list
        except Exception as e:
            logs.exception(e)

    def convertToCourse(self, course):
        try:
            course_object = Course(course['courseid'], course["coursecode"],
                                   course["coursedesc"], course["coursename"],
                                   course["courseduration"], course["courseimageurl"], )
            return course_object
        except Exception as e:
            logs.exception(e)


class CourseForm(FlaskForm):
    course_id = IntegerField('Course Id', validators=[DataRequired()])
    course_code = StringField('Course Code', validators=[DataRequired()])
    course_name = StringField('Course Name', validators=[DataRequired()])
    course_desc = StringField('Course Desc', validators=[DataRequired()])
    course_imageUrl = StringField('Course Image Url')
    course_duration = IntegerField('Course Duration', validators=[DataRequired()])
    submit = SubmitField('Add Course')
