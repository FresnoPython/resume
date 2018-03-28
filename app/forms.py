from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	subject = StringField('Subject', validators=[DataRequired()])
	content = TextAreaField('Content', validators=[DataRequired(),Length(min=1, max=280)])
	submit = SubmitField('Submit')
