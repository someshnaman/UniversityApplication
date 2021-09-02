from flask import Flask
from flask_bcrypt import Bcrypt

bcrypt = ""


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aeeb570f88a347bdb9193add0aa72612'
    # global bcrypt
    bcrypt = Bcrypt(app)

    from course.courseroute import course_blueprint
    from login.loginroute import login_blueprint
    app.register_blueprint(course_blueprint, url_prefix="/")
    app.register_blueprint(login_blueprint, url_prefix="/")
    return app
