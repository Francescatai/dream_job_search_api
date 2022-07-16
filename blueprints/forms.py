''' 封裝表單驗證 '''
import wtforms
from wtforms.validators import length, email, EqualTo
from projectapi.models import EmailCaptchaModel, UserModel

# 登入限制驗證
class LoginForm(wtforms.Form):
    # email要是email的格式
    email = wtforms.StringField(validators=[email()])
    password = wtforms.StringField(validators=[length(min=6, max=20)])

# 註冊限制驗證
class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=3, max=20)])
    email = wtforms.StringField(validators=[email()])
    captcha = wtforms.StringField(validators=[length(min=4, max=4)])
    password = wtforms.StringField(validators=[length(min=4, max=20)])
    # 密碼要等同於資料庫中的密碼
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    @staticmethod
    def validate_email(field):
        email1 = field.data
        user_model = UserModel.query.filter_by(email=email1).first()
        if user_model:
            raise wtforms.ValidationError("Email重複註冊！")

    def validate_captcha(self, field):
        captcha = field.data
        email1 = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email1).first()
        if not captcha_model or captcha_model.captcha.lower() != captcha.lower():
            raise wtforms.ValidationError("驗證碼錯誤！")

# 提問驗證
# 標題3-200字
# 內容最少5個字
class QuestionForm(wtforms.Form):
    title = wtforms.StringField(validators=[length(min=3, max=200)])
    content = wtforms.StringField(validators=[length(min=5)])

# 回答驗證-最少一個字
class AnswerForm(wtforms.Form):
    content = wtforms.StringField(validators=[length(min=1)])

