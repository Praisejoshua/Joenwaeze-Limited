from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from web.models import User


class LoginForm(FlaskForm):
       username = StringField(label = "User Name", validators= [DataRequired()])
       email = StringField(label="Email", validators= [DataRequired(), Email()] )
       password = PasswordField(label = "Password", validators=[DataRequired()])
       submit = SubmitField(label = "Sign In")


class ContactForm(FlaskForm):
       first_name = StringField(label="First Name", validators=[Length(min=5, max = 30), DataRequired()], render_kw={"placeholder" : "Enter Number"})
       last_name = StringField(label="Last Name", validators=[Length(min=5, max = 30), DataRequired()], render_kw={"placeholder" : "Enter Number"})
       email = StringField(label="Email Address", validators=[Email(), DataRequired()], render_kw={"placeholder" : "Enter your Email"})
       text = StringField(label="Message", validators=[Length(min=10, max=1024)], render_kw={"placeholder" : "Text Area"})
       submit = SubmitField(label="Submit")

class RegisterForm(FlaskForm):

       def validate_username (self, username_to_check):
              user = User.query.filter_by(username = username_to_check.data).first()
              if user:
                     raise ValidationError ("User name already exit. Please try another")

       def validate_email(self, email_to_check):
              email = User.query.filter_by(email = email_to_check.data).first()
              if email:
                     raise ValidationError("Email Address already exixt. Please try another")

       username = StringField(label = "User Name", validators= [DataRequired()])
       email = StringField(label="Email", validators= [DataRequired(), Email()] )
       password1 = PasswordField(label = "Password", validators=[Length(min = 6), DataRequired()])
       password2 = PasswordField(label = "Confirm Password", validators=[DataRequired(), EqualTo("password1")])
       submit = SubmitField(label = "Create Account")
