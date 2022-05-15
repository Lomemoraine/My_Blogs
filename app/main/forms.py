from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import InputRequired
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please share something interesting about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')