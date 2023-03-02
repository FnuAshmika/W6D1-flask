from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, DecimalField
from wtforms.validators import DataRequired, EqualTo

class RegisterForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password =PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords Must Match!!')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class BlogForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    blog = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Post')

class CarForm(FlaskForm):
    make= StringField('Make', validators=[DataRequired()])
    model = StringField('Model', validators=[DataRequired()])
    year = IntegerField('Year', validators=[DataRequired()])
    color = StringField('Color', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()]) 
    submit = SubmitField('Submit')    