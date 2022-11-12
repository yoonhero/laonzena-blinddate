from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(128))
    schoolNumber = db.Column(db.String(5))

    
    mbti = db.Column(db.String(10))
    bloodtype = db.Column(db.String(5))
    favoriteFood = db.Column(db.String(10))
    favoriteColor = db.Column(db.String(10))
    


    