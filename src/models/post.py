import datetime
from src.db.database import db


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    postUrl = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.now())
    updatedAt = db.Column(db.DateTime,onupdate=datetime.datetime.now())


    def __repr__(self) -> str:
        return f'Post title: {self.title}'

