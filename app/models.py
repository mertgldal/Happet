from . import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    animals = db.relationship("Animal", back_populates="creator")

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship("User", back_populates="animals")
    animal_name = db.Column(db.String(100), nullable=False)
    animal_type = db.Column(db.String(100), nullable=False)
    animal_gender = db.Column(db.String(100), nullable=False)
    animal_age = db.Column(db.Integer, nullable=False)
    animal_color = db.Column(db.String(100), nullable=False)
    history = db.Column(db.Text, nullable=False)
    character = db.Column(db.Text, nullable=False)
    behavioral_features = db.Column(db.Text, nullable=False)
    preferences = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    date_from = db.Column(db.Date, nullable=True)
    date_to = db.Column(db.Date, nullable=True)
