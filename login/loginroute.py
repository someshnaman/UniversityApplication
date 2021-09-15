from flask import render_template, url_for, flash, redirect, Blueprint
from flask import Flask, session
from route import bcrypt
from .forms import RegistrationForm, LoginForm
from .user import User, UserDao
from flask_login import login_user, current_user, logout_user, login_required
import uuid
login_blueprint = Blueprint("login_blueprint", __name__)


@login_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    try:
        if current_user.is_authenticated:
            return redirect(url_for('home_blueprint.home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            # here we're getting the data from UI and we'll create a User object with that
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user_list = [uuid.uuid4(), form.email.data, hashed_password, form.username.data]
            user_dao = UserDao()
            user_dao.insertUser(user_list)
            flash(f'Account created for {form.username.data}!', 'success')
            return redirect(url_for('course_blueprint.find'))

        return render_template('register.html', title='Register', form=form)
    except Exception as e:
        print(e)


@login_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_blueprint.home'))
    form = LoginForm()
    if form.validate_on_submit():
        # let's first check whether the user exist or not
        user_dao = UserDao()
        db_user_result = user_dao.findUserByEmail(form.email.data)
        if db_user_result is not None:
            if bcrypt.check_password_hash(db_user_result.password, form.password.data):
                print(db_user_result.is_active)
                login_user(db_user_result, remember=form.remember.data, force=True)
                print(db_user_result.is_authenticated)
                print(db_user_result.id)
                print(current_user.is_authenticated)
                # session['user_name'] = form.email.data

                return redirect(url_for('home_blueprint.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@login_blueprint.route("/logout")
def logout():
    session['user_name'] = None
    logout_user()
    return redirect(url_for('home_blueprint.home'))
