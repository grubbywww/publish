from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import Required,Length,Email

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,16),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Keep me Logged In')
    submit = SubmitField('GO')

