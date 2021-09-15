from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from itsdangerous.url_safe import URLSafeSerializer

bcrypt = Bcrypt()
login_manager = LoginManager()


def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'aeeb570f88a347bdb9193add0aa72612'
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.session_protection = "strong"
    from course.courseroute import course_blueprint
    from login.loginroute import login_blueprint
    from home.homeroute import home_blueprint
    app.register_blueprint(course_blueprint, url_prefix="/")
    app.register_blueprint(login_blueprint, url_prefix="/")
    app.register_blueprint(home_blueprint, url_prefix="/")
    return app
