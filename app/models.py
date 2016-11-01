from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(240), unique=True)
    password = db.Column(db.Unicode(240))
    update_time = db.Column(db.DateTime, index=True)
