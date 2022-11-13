from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    # username = StringField(label='Username', validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField(label='Email', validators=[DataRequired(), Email(), Length(min=4)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(max=30)])
    submit = SubmitField(label='Login')
