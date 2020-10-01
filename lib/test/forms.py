from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,Email,EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired('使用者名稱最少6個字母，最多20個'),Length(min=6,max=20)])
    email = StringField('Email',validators=[InputRequired('無效電子郵件'),Email()])
    password = PasswordField('Password',validators=[InputRequired('密碼最少8個，最多20個'),Length(min=8,max=20)])
    confirm = PasswordField('Repeat Password',validators=[InputRequired('密碼不符'),EqualTo('password')])
    submit = SubmitField('Register')
