from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import Email

class SignUpForm(FlaskForm):

    """email signup form"""
    email = EmailField(validators=[Email(message="Enter correct email address", granular_message=False)])
    submit = SubmitField("Sign Up")