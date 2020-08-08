import os
from flask import Flask
from . import db
from . import auth

def create_app(config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )
    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError as e:
        pass
    
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello World !'

    db.init_app(app)
    app.register_blueprint(auth.bp)


    return app
        