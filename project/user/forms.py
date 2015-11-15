# user/forms.py


from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(Form):
    email = TextField('Email Address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(Form):
    first_name = TextField('First Name',
                           validators=[DataRequired(),
                                       Length(max=50)])
    last_name = TextField('Last Name', validators=[Length(max=50)])
    email = TextField('Email Address',
                      validators=[DataRequired(),
                                  Email(message=None),
                                  Length(min=6, max=255)])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         Length(min=6, max=50)])
    confirm = PasswordField('Confirm password',
                            validators=[DataRequired(),
                                        EqualTo('password',
                                        message='Passwords must match.')])
