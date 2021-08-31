from flask import render_template, url_for, flash, redirect, Blueprint
from route import bcrypt
from .forms import RegistrationForm, LoginForm
from database.user import User
from database.cassandradatabase import Database
from database import constants
from route import bcrypt

login_blueprint = Blueprint("login_blueprint", __name__)


@login_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt(form.password.data).decode('utf-8')
        user = [form.email.data, hashed_password, form.username.data]
        database_object = Database()
        database_object.insert(constants.uery_insert_user, user)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


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
