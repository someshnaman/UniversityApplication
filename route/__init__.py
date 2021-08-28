from flask import Flask


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aeeb570f88a347bdb9193add0aa72612'
    from course.courseroute import course_blueprint
    app.register_blueprint(course_blueprint, url_prefix="/")
    return app

