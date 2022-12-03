import datetime
from db.database import db
# 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.Text,nullable=False)
    createdAt = db.Column(db.DateTime,default=datetime.now())
    updatedAt = db.Column(db.DateTime,onupdate=datetime.now())


    def __repr__(self) -> str:
        return 'User: {self.username}'

