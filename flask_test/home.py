#! /usr/bin/env python
#coding=utf-8

from flask import Flask, render_template
from flask import request
from flask import current_app
from flask import make_response
from flask import redirect, session
from flask import abort, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess!!'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    "mysql+pymysql://ahhxfeng:123456@192.168.141.139:3306/test"
manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
db.init_app(app)

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
        name = form.name.data
        form.name.data = ''
        session['name'] = name
        
        return redirect(url_for('index'))
        
    user_agent = request.headers.get('User-Agent')
    Broswer_info = '<p>Your browser is {0},current_name is {1}'.format(user_agent, current_app.name)
    response = make_response(
        # '<p>Your browser is {0},current_name is {1}'.format(user_agent, current_app.name), 
        render_template('index.html', form=form, name=session.get('name')), 200)
    # response_test = make_response('he',  300, '2000')
    response.set_cookie('answer', '42')
    return response
    # return '<p>Your browser is {0},current_name is {1}'.format(user_agent, current_app.name),200
    # return '<h1>hello world！</h1>'


@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello ,{0}</h1>'.format(name)

    if name is 'h':
        abort(404)
    response = make_response(redirect('http://www.baidu.com'), '<h1>Hello ,{0}</h1>'.format(name))
    response = make_response(render_template('./user.html', name=name))
    response.set_cookie('answer', '20')
    return response

if __name__ == "__main__":
    # app.run(debug=True)
    manager.run()
