from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
import sqlalchemy as sa
from app import db
from app.models import User
from flask_babel import _, lazy_gettext as _l
       
class EditProfileForm(FlaskForm):
    username = StringField(_l('使用者名稱'), validators=[DataRequired()])
    about_me = TextAreaField(_l('關於我'), validators=[Length(min=0,max=200)])
    submit = SubmitField(_l('修改'))

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(User.username == self.username.data))
            if user is not None:
                raise ValidationError(_l('該使用者名稱已有人使用'))
            
class EmptyForm(FlaskForm):
    submit = SubmitField(_l('提交'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('說點什麼...'),validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('發佈'))