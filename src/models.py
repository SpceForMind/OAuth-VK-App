from src.app import db
from src.app import lm
from flask_login import UserMixin


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    friends = db.relationship('Friend', backref='is_friends', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.id)


class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    is_friends_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Friend {}> of the <User {}>'.format(self.id, self.is_friends_id)
