# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Email

# contact form
class ContactForm(FlaskForm):
    name = StringField("name", validators = [DataRequired()])
    email = StringField("email", validators = [DataRequired(), Email()])
    copy = BooleanField('copy')
    human = BooleanField('human', validators = [DataRequired()])
    message = StringField('message', validators = [DataRequired()])
