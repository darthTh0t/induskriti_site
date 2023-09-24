from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField, StringField
from wtforms.validators import Email, DataRequired

class SignUpForm(FlaskForm):

    """email signup form"""
    name = StringField(validators=[DataRequired("Please enter a valid name")])
    email = EmailField(validators=[Email(message="Enter correct email address", granular_message=False)])
    submit = SubmitField("Sign Up")