from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _l
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
import sqlalchemy as sa 
from app import db
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('使用者名稱'),validators=[DataRequired()])
    password = PasswordField(_l('密碼'),validators=[DataRequired()])
    remember_me = BooleanField(_l('記住我'))
    submit = SubmitField(_l('登入'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('使用者名稱'), validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(_l('密碼'), validators=[DataRequired()])
    password2 = PasswordField(_l('再輸入一次密碼'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('註冊'))

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError(_l('該使用者名稱已存在'))
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError(_l('該 email 已存在'))
        
class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('重設密碼'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('密碼'), validators=[DataRequired()])
    password2 = PasswordField(_l('再輸入一次密碼'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('重設密碼'))