#!/usr/bin/env python
# encoding utf-8

from flask import Flask, redirect, request, url_for, session, flash, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo
import fc

app = Flask(__name__)
app.config.from_object(fc)
manager = Manager(app=app)
db = SQLAlchemy(app)
app.secret_key = 'zaq1@WSX'

class NewsForm(FlaskForm):
    name = StringField(label='姓名', validators=[DataRequired("请输入姓名")], description="请输入姓名")
    age = StringField(label='年龄', validators=[DataRequired("请输入年龄")], description="请输入年龄")
    submit = SubmitField('提交')

app.secret_key = "zaq1@WSX"

class Man(db.Model):
    __tablename__ = 'mans'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(200), nullable=False)

db.create_all()

@app.route('/add',methods=["GET", "POST"])
def add():
    form = NewsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_obj = Man(              # 使用flask-sqlalchemy定义的一个表结构
                name = form.name.data,  #form后面是模板定义的,要保持一致
                age = form.age.data
            )
            db.session.add(new_obj)
            db.session.commit()
            return redirect(url_for('get'))
    return render_template('f.html',form=form)

@app.route('/get')
def get():
    mans = Man.query.all()
    return render_template('gf.html', mans=mans)

if __name__ == '__main__':
    manager.run()