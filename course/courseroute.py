from flask import Blueprint, Flask
from .coursemodel import CourseDao
from flask import render_template
import json

course_blueprint = Blueprint("course_blueprint", __name__)


@course_blueprint.route('/find', methods=['GET'])
def find():
    course_object = CourseDao()
    result = course_object.findAllCourses()
    return render_template("find.html", result=result)
