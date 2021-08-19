from flask import Flask


def createApp():
    app = Flask(__name__)

    from course.courseroute import course_blueprint
    app.register_blueprint(course_blueprint, url_prefix="/")
    return app
