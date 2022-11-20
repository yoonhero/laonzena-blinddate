import datetime

from database.index import db


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    payload = db.Column(db.String(128))

    # Relationship
    # user = db.relationship("User", back_populates="messages")
    # room = db.relationship("Room", back_populates="messages")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    createdAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    roomId = db.Column(db.Integer, db.ForeignKey("room.id"))
    read = db.Column(db.Boolean, default=False)

    def __init__(self, payload, user, room, roomId):
        self.payload = payload
        self.user_id = user
        self.room = room
        self.roomId = roomId
