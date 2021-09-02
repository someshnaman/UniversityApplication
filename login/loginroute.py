from flask import render_template, url_for, flash, redirect, Blueprint
from route import bcrypt
from .forms import RegistrationForm, LoginForm
from database.cassandradatabase import Database
from database import constants
from route import bcrypt
from .user import User

login_blueprint = Blueprint("login_blueprint", __name__)


@login_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    try:
        form = RegistrationForm()
        if form.validate_on_submit():
            # hashed_password = bcrypt(form.password.data).decode('utf-8')
            # here we're getting the data from UI and we'll create a User object with that
            user_details_from_ui = User(form.email.data, form.password.data,
                                        form.username.data)
            user_list = [user_details_from_ui.id, user_details_from_ui.email,
                         user_details_from_ui.password, user_details_from_ui.username]
            database_object = Database()
            database_object.insert(constants.uery_insert_user, user_list)
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('course_blueprint.find'))

        return render_template('register.html', title='Register', form=form)
    except Exception as e:
        print(e)


@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':

            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
