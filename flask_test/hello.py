#! /usr/bin/env pytthon
#coding=utf-8

__author__ = 'ahhxfeng'
__version__ = '1.0.0'

from flask import Flask, render_template
from flask_script import Manager
# from flask_bootstrp import Bootstrap
from flask_bootstrap import bootstrap_find_resource

app = Flask(__name__)
Manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    # return '<h1>Hello world !!!</h1>'
    return render_template('index.html')

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

