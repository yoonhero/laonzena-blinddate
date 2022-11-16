from database.index import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    # Using When User Login
    password = db.Column(db.String(128), nullable=False)
    schoolNumber = db.Column(db.String(5), unique=True, nullable=False)

    # User Information
    ## TODO: AGE
    gender = db.Column(db.String(10))
    mbti = db.Column(db.String(10))
    bloodtype = db.Column(db.String(5))
    favoriteFood = db.Column(db.String(10))
    favoriteColor = db.Column(db.String(10))

    # Create USER

    def __init__(self, password, schoolNumber):
        self.password = password
        self.schoolNumber = schoolNumber
