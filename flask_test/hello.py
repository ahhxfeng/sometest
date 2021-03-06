#! /usr/bin/env python
#coding=utf-8

__author__ = 'ahhxfeng'
__version__ = '1.0.0'

from flask import Flask, render_template
from flask_script import Manager
# from flask_bootstrp import Bootstrap
from flask_bootstrap import bootstrap_find_resource
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('what is your name ?', validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is hard to guess string'
Manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return '<h1>Hello world !!!</h1>'
    name = None
    form = NameForm()
    if form.validator_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name )

@app.route('/user/<name>')
def user(name):
    # return '<h1>Hello %s</h1>' % name
    return render_template('user.html', name=name)

@app.route('/bad')
def badtest():
    # return '<h1>bad test</h1>', 400
    return render_template('bad.html'), 400

if __name__ == "__main__":
    # app.run(debug=True)
    Manager.run()


