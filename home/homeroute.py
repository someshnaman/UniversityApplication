from flask import Blueprint, render_template

home_blueprint = Blueprint('home_blueprint', __name__)


@home_blueprint.route('/')
@home_blueprint.route('/home')
def home():
    return render_template('home.html')
