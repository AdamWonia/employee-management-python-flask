from my_app import db
from flask_login import UserMixin


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    position = db.Column(db.String(100))

    def __init__(self, name, surname, email, phone, position):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.position = position

    def __str__(self):
        return f'{self.name}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.username}'
