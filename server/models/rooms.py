import datetime

from database.index import db


class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)

    users = db.relationship("User", back_populates="messages")
    messages = db.relationship("Message", back_populates="room")

    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
