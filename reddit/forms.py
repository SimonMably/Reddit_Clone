from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, TextAreaField, SearchField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, URL, Length, EqualTo, Email, ValidationError

#from reddit.models import User


class RegisterUserForm(FlaskForm):
    
    username = StringField(
        label="Username: ",
        validators=[Length(min=3, max=20), DataRequired()]
    )
    email_address = StringField(
        label="Email Adress: ", 
        validators=[Email(), DataRequired()]
    )
    password = PasswordField(
        label="Password: ", 
        validators=[Length(min=6), DataRequired()]
    )
    confirm_password = PasswordField(
        label="Confirm Password: ",
        validators=[EqualTo("password"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")
    
    def validate_username(self, username_check):
        """"""
        user = User.query.filter_by(username=username_check.data).first()
        
        if user:
            raise ValidationError("That username is already in use. Please try a different username.")
    
    def validate_email_address(self, email_address_check):
        """"""
        email_address = User.query.filter_by(email=email_address_check.data).first()
        
        if email_address:
            raise ValidationError("That email address is already in use. Please try a different email address.")


class LoginUserForm(FlaskForm):
    
    username = StringField(label="User Name", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField(label="Submit")


class CreatePost(FlaskForm):
    pass


class CreateComment(FlaskForm):
    pass

