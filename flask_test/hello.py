#! /usr/bin/env pytthon
#coding=utf-8

__author__ = 'ahhxfeng'
__version__ = '1.0.0'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world !!!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s</h1>' % name

@app.route('/bad')
def badtest():
    return '<h1>bad test</h1>', 400

if __name__ == "__main__":
    app.run(debug=True)

