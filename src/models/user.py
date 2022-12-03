import datetime
from src.db.database import db

 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    passwordHash = db.Column(db.Text,nullable=False)
    createdAt = db.Column(db.DateTime,default=datetime.datetime.now())
    updatedAt = db.Column(db.DateTime,onupdate=datetime.datetime.now())

   
    def __repr__(self) -> str:
        return 'User: {self.username}'
