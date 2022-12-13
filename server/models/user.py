from database.index import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    # Using When User Login
    password = db.Column(db.String(128), nullable=False)
    schoolNumber = db.Column(db.String(5), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(15), nullable=False)

    # User Information
    ## TODO: AGE
    age = db.Column(db.String(10))
    gender = db.Column(db.String(10))
    mbti = db.Column(db.String(10))
    bloodtype = db.Column(db.String(5))
    favoriteFood = db.Column(db.String(10))
    favoriteColor = db.Column(db.String(10))

    # Matched Relation with SchoolNumber
    matchedUser = db.Column(db.String(5))
    matched = db.Column(db.Boolean, default=False)

    # TODO: For Chatting
    messages = db.relationship("Message", backref="user")
    roomId = db.Column(db.Integer, db.ForeignKey("room.id"))

    def __init__(self, password, schoolNumber):
        self.password = password
        self.schoolNumber = schoolNumber

    def __repr__(self):
        return f"<Post {self.schoolNumber}>"
