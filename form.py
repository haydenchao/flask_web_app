from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask import Flask



class CommentForm(FlaskForm):
    ## Form elements initialized here
    comment = StringField("Comments", validators=[DataRequired()])
    submit = SubmitField("Sent")
