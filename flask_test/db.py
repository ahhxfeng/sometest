from flask_sqlalchemy import SQLAlchemy
from home import app

db = SQLAlchemy(app)


class Role(db.Model):
    