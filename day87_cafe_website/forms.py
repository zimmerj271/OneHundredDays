from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField


class AddCafeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    coffee_price = StringField("Price for Coffee", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    map_url = StringField("Google Map URL", validators=[DataRequired(), URL()])
    seats = StringField("Number of Seats", validators=[DataRequired()])
    has_toilet = BooleanField("Toilet")  # Do not add validators for BooleanField
    has_wifi = BooleanField("Wifi")
    has_sockets = BooleanField("Power Outlet")
    can_take_calls = BooleanField("Can Take Calls")
    submit = SubmitField("Submit Post")


# Create Registration Form
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
