from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    
    # Content field will now store the HTML (including images or videos) from Quill.js
    content = TextAreaField('Content', validators=[DataRequired()])  # Will handle HTML content
    
    submit = SubmitField('Post')
