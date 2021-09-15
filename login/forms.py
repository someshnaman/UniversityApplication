from .user import UserDao
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from database.logger import Logs

logs = Logs()


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=6, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password'), Length(min=6, max=20)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user_db_object = UserDao()
        email_result = user_db_object.findUserByEmail(self.email.data)
        if email_result is None:
            return False
        elif email_result.username == self.username.data:
            raise ValidationError('This Username is taken. Please chose another one')

    def validate_email(self, email):
        user_db_object = UserDao()
        email_result = user_db_object.findUserByEmail(self.email.data)
        if email_result is None:
            return False
        elif email_result.email == email.data:
            raise ValidationError('This email is taken. Please chose another one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
