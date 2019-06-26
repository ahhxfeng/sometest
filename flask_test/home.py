#! /usr/bin/env python
#coding=utf-8

__author__ = 'ahhxfeng'
__version__ = '1.0.0'
import os

from flask import Flask, render_template, request, current_app, make_response, redirect, session, abort, url_for, flash
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess!!'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://ahhxfeng:123456@localhost:3306/test"
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[FLASKY]'
app.config['FLASKY_MAIL_SENDER'] = 'Flaky admin <779107975@qq.com>'
app.config['MAIL_SERVER'] = 'stmp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '779107975@qq.com'
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_PASSWORD'] = 'zuhhszjaokwpbefj'
manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)
mail = Mail(app)


class NameForm(FlaskForm):
    name = StringField('what is your name ?', validators=[Required()])
    password = PasswordField('input Passoword', validators=[Required()])
    submit = SubmitField('Submit')

class Role(db.Model):
    __tablename__ = 'roles' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name

    users = db.relationship('User', backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
    
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and form.name.data != old_name:
            flash('look like you have change your name')
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            send_mail(app.config['MAIL_USERNAME'], 'NEW USER', 'mail/new_user', user=user)
        else:
            session['known'] = True
        name = form.name.data
        form.name.data = ''
        session['name'] = name
        
        return redirect(url_for('index'))
        
    user_agent = request.headers.get('User-Agent')
    Broswer_info = '<p>Your browser is {0},current_name is {1}'.format(user_agent, current_app.name)
    response = make_response(
        render_template('index.html', form=form, name=session.get('name'),
                         known=session.get('known', False)),
                          200)
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello ,{0}</h1>'.format(name)

    if name is 'h':
        abort(404)
    response = make_response(redirect('http://www.baidu.com'), '<h1>Hello ,{0}</h1>'.format(name))
    response = make_response(render_template('./user.html', name=name))
    response.set_cookie('answer', '20')
    return response

def make_shell_context():
    return dict(app=app, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)

if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
