from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    Name = StringField('Name', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    Subject = StringField('Subject', validators=[DataRequired(), Length(max=100)])
    Message = TextAreaField('Message', validators=[DataRequired(), Length(max=500)])
        

