from .user import UserDbQueries
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validateUsername(self):
        user_db_object = UserDbQueries()
        email_result = user_db_object.findUserByEmail(self.email.data)
        if email_result.username == self.username.data:
            raise ValidationError('This Username is taken. Please chose another one')

    def validateEmail(self):
        user_db_object = UserDbQueries()
        email_result = user_db_object.findUserByEmail(self.email.data)
        if email_result.email == self.email.data:
            raise ValidationError('This email is taken. Please chose another one')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
