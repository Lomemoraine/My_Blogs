from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField,StringField
from wtforms.validators import InputRequired,DataRequired

from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Please share something interesting about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    
class PostForm(FlaskForm):
    post_title = StringField('Blog Title', validators=[DataRequired()])
    post_content = TextAreaField('Blog Content', validators=[DataRequired()])
    submit = SubmitField('Submit Post')
    
class UpdatePostForm(FlaskForm):
    post_title = StringField("Blog title", validators=[DataRequired()])
    post_content = TextAreaField("Type Away", validators=[DataRequired()])
    submit = SubmitField("Update Blog")
    
class CommentForm(FlaskForm):
    comment = TextAreaField("Blog Comment", validators=[DataRequired()])
    alias = StringField("Comment Alias")# to hide user's identity
    submit = SubmitField("Comment")
