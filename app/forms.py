from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.fields.html5 import DateField

class RegistrationForm(FlaskForm): #create RegistrationForm class which inherits from FlaskForm
    username = StringField("Username")
    email = StringField("Email")
    emailCheck = StringField("Repeat Email")
    password = PasswordField("Password")
    passwordCheck = PasswordField("Repeat Password")
    dateOfBirth = DateField("Date of Birth", format="%d/%m/%Y")
    gender = SelectField("Gender", choices=[("m", "Male"), ("f", "Female"), ("o", "Other")])
    submit = SubmitField("Register")

