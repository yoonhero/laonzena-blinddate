from database.index import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Using When User Login
    password = db.Column(db.String(128), nullable=False)
    schoolNumber = db.Column(db.String(5), unique=True, nullable=False)

    # User Information
    ## TODO: AGE
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    mbti = db.Column(db.String(10))
    bloodtype = db.Column(db.String(5))
    favoriteFood = db.Column(db.String(10))
    favoriteColor = db.Column(db.String(10))

    # Matched Relation with SchoolNumber
    matchedUser = db.Column(db.String(5))

    # TODO: For Chatting
    messages = db.relationship("Message", back_populates="user")
    rooms = db.relationship("Room", back_populates="users")

    def __init__(self, password, schoolNumber):
        self.password = password
        self.schoolNumber = schoolNumber
