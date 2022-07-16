from projectapi.exts import db
from datetime import datetime

''' Email驗證 '''
class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    captcha = db.Column(db.String(10), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)

''' 用戶 '''
class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    join_time = db.Column(db.DateTime, default=datetime.now)

''' 討論區-提問 '''
class QuestionModel(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    author = db.relationship("UserModel", backref="questions")

''' 討論區-回答 '''
class AnswerModel(db.Model):
    __tablename__ = "answer"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    question = db.relationship("QuestionModel", backref=db.backref("answers", order_by=create_time.desc()))
    author = db.relationship("UserModel", backref="answers")

''' 職缺資訊 '''
class JobModel(db.Model):
    __tablename__ = "job"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jobtitle = db.Column(db.String(200), nullable=False)
    joburl = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    minsalary = db.Column(db.Integer)
    maxsalary = db.Column(db.Integer)
    skill = db.Column(db.String(200))
    jd = db.Column(db.Text)
    jr = db.Column(db.Text)
    walfare = db.Column(db.Text)
    source = db.Column(db.String(200))
    updatetime = db.Column(db.DateTime)
