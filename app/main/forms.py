from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('Who do you want to search?', validators=[Required()])
    submit = SubmitField('Submit')
