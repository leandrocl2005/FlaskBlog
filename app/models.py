from app import db
from app import login
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    social_id = db.Column(
        db.String(64),
        nullable=False,
        unique=True,
        default=""
    )
    bio = db.Column(db.String(255), default="Uma pessoa muito legal.")
    pic = db.Column(db.String(255), default="img/avatar.png")

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    slug = db.Column(db.String(8), nullable=False)
    css_class = db.Column(db.String(5), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug
        }

    def __repr__(self):
        return '<Categoria {}>'.format(self.name)


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.String(5000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))
    publish_date = db.Column(db.DateTime, default=datetime.utcnow)
    pic = db.Column(db.String(255), default="img/post-1.jpg")
    abstract = db.Column(db.String(100))
    featured = db.Column(db.Boolean, default=False)
    start_page = db.Column(db.Boolean, default=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'user_id': self.user_id,
            'abstract': self.abstract,
            'publish_date': "{}/{}/{}".format(
                self.publish_date.day,
                self.publish_date.month,
                self.publish_date.year
            )
        }

    def __repr__(self):
        return '<Post {}>'.format(self.name)
