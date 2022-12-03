import datetime
from db.database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    postUrl = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.DateTime,default=datetime.now())
    updatedAt = db.Column(db.DateTime,onupdate=datetime.now())


    def __repr__(self) -> str:
        return 'Post title: {self.title}'

