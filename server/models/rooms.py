import datetime

from database.index import db


class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)

    messages = db.relationship("Message", backref="room")
    users = db.relationship("User", backref="room")

    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
