from flask import Blueprint, redirect, url_for, flash
from flask import render_template

from .coursemodel import CourseDao, CourseForm

course_blueprint = Blueprint("course_blueprint", __name__)


@course_blueprint.route('/course', methods=['GET'])
def find():
    course_object = CourseDao()
    result = course_object.findAllCourses()
    return render_template("course_list.html", course_list=result)


@course_blueprint.route("/course/<int:course_id>")
def post(course_id):
    course_object = CourseDao()
    result = course_object.findCourseById(course_id)
    return render_template("course.html", course_object=result)


@course_blueprint.route("/course/new", methods=['GET', 'POST'])
def addCourse():
    form = CourseForm()
    if form.validate_on_submit():
        course_to_be_inserted = [form.course_id.data, form.course_code.data,
                                 form.course_name.data, form.course_desc.data,
                                 form.course_imageUrl.data, form.course_duration.data]
        course_insert = CourseDao()
        course_insert.insertCourse(course_to_be_inserted)
        flash(f"Course has been successfully inserted", "success")
        return redirect(url_for('course_blueprint.find'))
    return render_template('add-course.html', title='Add Course', form=form)
