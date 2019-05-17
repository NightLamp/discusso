from app import login
from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    bio = db.Column(db.String(248))
    passwd_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    admin = db.Column(db.Boolean)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    replies = db.relationship('Reply', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<id {}, User {}>'.format(self.id, self.username)

    def set_password(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.passwd_hash, password)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    desc = db.Column(db.String(248))
    blesses = db.Column(db.Integer, default=0)
    curses = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    p_replies = db.relationship('Reply', backref='ogPost', lazy='dynamic')

    def __repr__(self):
        return '<id {}, Post {}>'.format(self.id, self.title)


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
#     reply_id  = db.Column(db.Integer, db.ForeignKey('reply.id'))
    text = db.Column(db.String(248))
    blesses = db.Column(db.Integer, default=0)
    curses = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    stance = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # r_replies   = db.relationship('Reply', backref='ogPost', lazy='dynamic')

    def __repr__(self):
        return '<id {}, Reply {}>'.format(self.id, self.text)


# Old code from mega tutorial
'''
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
'''
